import os
import uuid
import json
import logging
from collections import OrderedDict
from dotenv import load_dotenv
from typing import Optional
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from powerdict.api import authentication

from powerdict import schemas, frictionless, db, files

load_dotenv()
bucket_name = os.environ['S3_BUCKET_FRICTIONLESS']

db_client = db.get_db_client()


router = APIRouter(tags=["Frictionless"])


@router.get(
    '/data-packages/metadata',
    response_model=list[schemas.DataPackage],
    response_model_exclude_none=True,
    status_code=200
)
async def get_data_package_metadata(
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_packages = db_client.get_all_data_packages('dict')
    return data_packages


@router.get(
    '/data-packages/metadata/{data_package_id}',
    response_model=schemas.DataPackage,
    response_model_exclude_none=True,
    status_code=200
)
async def get_data_package_metadata(
    data_package_id: str,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_package = db_client.get_data_package(data_package_id, return_type='dict')

    return data_package


@router.post(
    '/data-packages/metadata',
    response_model=uuid.UUID,
    status_code=200
)
async def post_data_package_metadata(
    data_package: schemas.DataPackage,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_package = frictionless.save_fd_package_to_db(data_package, db_client)
    return data_package.data_package_id


@router.post(
    '/data-packages',
    response_model=uuid.UUID,
    status_code=200
)
async def post_data_package_fp(
    data_package_fp: str,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    bucket_name = os.environ['S3_BUCKET_FRICTIONLESS']
    
    try:
        with open(data_package_fp, 'r') as f:
            raw_data_package = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f'Could not find file at {data_package_fp}')
    except IsADirectoryError:
        raise HTTPException(status_code=400, detail='Could not save data package resource as file is a directory')

    data_package_dir = '/'.join(data_package_fp.split('/')[:-1])

    try:
        s3_filenames_to_resource_records = OrderedDict(
            (
                frictionless.resource_to_s3_filename(resource),
                frictionless.get_resource_records(resource, data_package_dir)
            )
            for resource 
            in raw_data_package['resources']
        )
    except frictionless.DuplicatedIndexError as e:
        raise HTTPException(status_code=400, detail=str(e))

    resource_filenames_to_fileobjs = OrderedDict(
        (
            frictionless.resource_to_s3_filename(resource),
            frictionless.get_resource_fileobj(resource, data_package_dir)
        )
        for resource 
        in raw_data_package['resources']
    )

    try:
        data_package = frictionless.save_fd_metadata_and_resources_to_db(raw_data_package, s3_filenames_to_resource_records, db_client)
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'Could not save data package to database due to `IntegrityError`')
    except frictionless.TableNotEmptyError:
        raise HTTPException(status_code=400, detail=f'Could not save data package resource as table already exists')

    files.upload_local_datapackage_to_s3(bucket_name, raw_data_package, resource_filenames_to_fileobjs, data_package.data_package_id)
    
    return data_package.data_package_id

# @router.post(
#     '/data-packages/',
#     response_model=dict[str, dict],
#     status_code=200
# )
# async def post_data_package(
#     file: UploadFile,
#     datapackage_filename: Optional[str] = None,
# ):
#     # should accept a .json that points to a .csv on the web, or a .zip that contains a .json and a .csv
#     # files should be saved to an S3 bucket
#     # the .json should be updated so that the resources point to the S3 bucket
#     # the .json should be saved to the database
#     # the .csv should be saved to the database
#     import zipfile
     
#     zipfile_ob = zipfile.ZipFile(file.file)
#     file_names = zipfile_ob.namelist()

#     if datapackage_filename is None:
#         json_file_names = [file_name for file_name in file_names if file_name.endswith('.json')]
#         assert len(json_file_names) == 1, f'Expected 1 .json file containing the datapackage metadata, found {len(json_file_names)}: {", ".join(json_file_names)}'
#         datapackage = json.loads(zipfile_ob.open(json_file_names[0]).read())
#     else:
#         datapackage = json.loads(zipfile_ob.open(datapackage_filename).read())
    
#     csv_file_names = [file_name for file_name in file_names if file_name.endswith('.csv')]
#     assert len(csv_file_names) > 0, f'Expected at least 1 .csv file containing tabular data, found none'

#     # files = [(zipfile_ob.open(name).read(),name) for name in json_file_names+csv_file_names]
#     # print(type(files[0]))
    
#     return {"filenames": datapackage}

@router.get(
    '/db-schema/{table_name}',
    status_code=200
)
async def get_db_schema(
    table_name: str,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    if table_name not in db.table_name_to_schema:
        raise HTTPException(status_code=404, detail=f'Could not find table {table_name} in database')
    
    table_schema = db.table_name_to_schema[table_name]
    
    return table_schema.schema()
