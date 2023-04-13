from fastapi import APIRouter, Depends
from powerdict.api import authentication

from powerdict import schemas
from powerdict.api.db import db_client


router = APIRouter(tags=["Frictionless"])

@router.get(
    '/hello',
    response_model=dict[str, str],
    status_code=200
)
async def hello(
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    return {'msg': f'hello {current_user.username}'}

@router.get(
    '/data-packages',
    response_model=list[schemas.DataPackage],
    status_code=200
)
async def get_data_packages(
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
):
    data_packages = db_client.get_all_data_packages('dict')
    return data_packages
