import os
import boto3
import uuid
import json
import shutil
import logging
from collections import OrderedDict
from typing import Optional, Union
from dotenv import load_dotenv
from io import BytesIO
from abc import ABC, abstractmethod


class FileStorage(ABC):
    @abstractmethod
    def __init__(cls, root_dir: str):
        pass

    @abstractmethod
    def create_folder(cls, folder_name: str):
        pass

    @abstractmethod
    def list_files(cls, folder_name: Optional[str] = None):
        pass

    @abstractmethod
    def upload_file(
        cls,
        data: Union[str, BytesIO],
        file_name: Optional[str] = None,
        folder_name: Optional[str] = None
    ):
        pass

    @abstractmethod
    def upload_files(
        cls,
        files: list[Union[str, BytesIO]],
        file_names: Optional[list[str]] = None,
        folder_name: Optional[str] = None
    ):
        pass


class LocalFileStorage(FileStorage):
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

    def create_folder(self, folder_name: str):
        if not isinstance(folder_name, str):
            raise TypeError('folder_name must be a string')
        os.makedirs(os.path.join(self.root_dir, folder_name), exist_ok=True)

    def list_files(self, folder_name: Optional[str] = None):
        if folder_name is None:
            folder_name = self.root_dir
        else:
            folder_name = os.path.join(self.root_dir, folder_name)
        if not os.path.isdir(folder_name):
            raise ValueError(f'{folder_name} is not a directory')
        return os.listdir(folder_name)

    def upload_file(self, data: Union[str, BytesIO], file_name: Optional[str] = None, folder_name: Optional[str] = None):
        if file_name is None:
            if isinstance(data, BytesIO):
                raise ValueError('You must specify a file name if you are uploading a BytesIO object')
            file_name = os.path.basename(data)

        if folder_name is not None:
            dest_path = os.path.join(self.root_dir, folder_name, file_name)
        else:
            dest_path = os.path.join(self.root_dir, file_name)

        if os.path.exists(dest_path):
            raise FileExistsError(f'{dest_path} already exists')

        if isinstance(data, str):
            shutil.copyfile(data, dest_path)
        elif isinstance(data, BytesIO):
            with open(dest_path, 'wb') as f:
                f.write(data.getvalue())
        else:
            raise ValueError("Data should be either a file path (str) or a BytesIO object")

    def upload_files(self, files: list[Union[str, BytesIO]], file_names: Optional[list[str]] = None, folder_name: Optional[str] = None):
        if file_names is None:
            file_names = [None] * len(files)

        if len(files) != len(file_names):
            raise ValueError("The number of files and file names must be the same")

        for file, file_name in zip(files, file_names):
            self.upload_file(file, file_name, folder_name)
            
    
class S3FileStorage(FileStorage):
    def __init__(
        cls,
        root_dir: str,
        region_name: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None
    ):
        cls.root_dir = root_dir

        load_dotenv()

        if region_name is None:
            region_name = os.environ['AWS_DEFAULT_REGION']

        if aws_access_key_id is None:
            aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']

        if aws_secret_access_key is None:
            aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

        cls.s3 = boto3.client(
            service_name='s3',
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def create_folder(
        cls,
        folder_name: str
    ):
        cls.s3.put_object(
            Bucket=cls.root_dir,
            Key=(str(folder_name)+'/')
        )

    def list_files(
        cls,
        folder_name: Optional[str] = None
    ):
        if folder_name is not None:
            prefix = folder_name + '/'
        else:
            prefix = ''

        response = cls.s3.list_objects_v2(
            Bucket=cls.root_dir,
            Prefix=(prefix)
        )

        return [file['Key'] for file in response['Contents']]
    
    def upload_file(
        cls,
        data: Union[str, BytesIO],
        file_name: Optional[str] = None,
        folder_name: Optional[str] = None
    ):
        if file_name is None:
            if isinstance(data, BytesIO):
                raise ValueError('You must specify a file name if you are uploading a BytesIO object')
            file_name = os.path.basename(data)

        if folder_name is not None:
            key = str(folder_name) + '/' + file_name
        else:
            key = ''
        
        if isinstance(data, str):
            cls.s3.upload_file(data, cls.root_dir, key)
        elif isinstance(data, BytesIO):
            cls.s3.upload_fileobj(data, cls.root_dir, key)
        else:
            raise ValueError("Data should be either a file path (str) or a BytesIO object")
    
    def upload_files(
        cls,
        files: list[Union[str, BytesIO]],
        file_names: Optional[list[str]] = None,
        folder_name: Optional[str] = None
    ):
        if file_names is None:
            file_names = [None] * len(files)
        
        if len(files) != len(file_names):
            raise ValueError("The number of files and file names must be the same")

        for file, file_name in zip(files, file_names):
            cls.upload_file(file, file_name, folder_name)


def upload_local_datapackage_to_s3(
    bucket_name: str,
    datapackage_dict: dict,
    resource_filenames_to_fileobjs: OrderedDict,
    data_package_id: str = str(uuid.uuid4())
):
    datapackage_io = BytesIO(json.dumps(datapackage_dict).encode('utf-8'))

    s3_client = S3FileStorage(bucket_name)
    s3_client.create_folder(data_package_id)
    s3_client.upload_file(datapackage_io, 'datapackage.json', data_package_id)

    if 'resources' in datapackage_dict.keys():
        s3_client.upload_files(
            resource_filenames_to_fileobjs.values(), 
            resource_filenames_to_fileobjs.keys(), 
            folder_name=data_package_id
        )


def upload_remote_datapackage_to_s3(
    bucket_name: str,
    datapackage_dict: dict,
    data_package_id: str = str(uuid.uuid4())
):
    pass
