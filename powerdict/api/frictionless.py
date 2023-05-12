import uuid
import json
import logging
from typing import Optional
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from powerdict.api import authentication

from powerdict import schemas, frictionless, db


db_client = db.get_db_client()


router = APIRouter(tags=["Frictionless"])

@router.get(
    '/hello',
    response_model=dict[str, str],
    status_code=200,
    include_in_schema=False
)
async def hello(
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    return {'msg': f'hello {current_user.username}'}

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
    try:
        data_package = frictionless.fd_fp_to_saved_metadata_and_resources(data_package_fp, db_client)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f'Could not find file at {data_package_fp}')
    
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