import uuid
import json
import logging

from fastapi import APIRouter, Depends
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
    '/data-packages',
    response_model=list[schemas.DataPackage],
    response_model_exclude_none=True,
    status_code=200
)
async def get_data_packages(
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_packages = db_client.get_all_data_packages('dict')
    return data_packages

@router.get(
    '/data-packages/{data_package_id}',
    response_model=schemas.DataPackage,
    response_model_exclude_none=True,
    status_code=200
)
async def get_data_package(
    data_package_id: str,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_package = db_client.get_data_package(data_package_id, return_type='dict')
    return data_package

@router.post(
    '/data-packages',
    response_model=uuid.UUID,
    status_code=200
)
async def post_data_packages(
    data_package: schemas.DataPackage,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    # for i, resource in enumerate(data_package['resources']):
    #     if 'schema' in resource.keys():
    #         resource['fd_schema'] = resource.pop('schema')

    # add a validator to DataPackage that does the schema -> fd_schema conversion

    data_package = frictionless.save_fd_package_to_db(data_package, db_client)
    return data_package.data_package_id
