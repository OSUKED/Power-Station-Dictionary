import uuid
import json
import logging
from typing import Any

from fastapi import APIRouter, Depends
from powerdict.api import authentication

from powerdict import schemas, dictionary, db


db_client = db.get_db_client()


router = APIRouter(tags=["Dictionary"])

@router.get(
    '/asset/{osuked_id}',
    response_model=schemas.AssetData,
    status_code=200
)
async def get_asset_data(
    osuked_id: int,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user),
) -> schemas.AssetData:
    """Retrieves asset data linked to the `osuked_id`"""
    source_links = db_client.get_all('dict__source_link')
    site_data = dictionary.load_site_data(osuked_id, db_client, source_links)
    
    return site_data


@router.post(
    '/asset',
    response_model=dict,
    status_code=200
)
async def post_new_asset(
    new_asset: schemas.NewAsset,
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user)
):
    """Creates a new OSUKED asset of the specified type and name"""
    return db_client.add_new_asset(new_asset)


@router.post(
    '/asset/link-ids/{osuked_id}',
    response_model=schemas.AssetIds,
    status_code=200
)
async def post_new_linked_ids(
    osuked_id: int,
    linked_ids: dict[str, list[Any]],
    current_user: schemas.SecureAPIUser = Depends(authentication.get_current_active_user)
) -> schemas.AssetIds:
    """Links associated IDs to an existing OSUKED asset
    
    Linked external ids can only be associated with a single asset, if a different asset is already linked to
    a submitted external id then the existing asset will be unlinked. If you believe that both assets
    should be linked to the same external id then look into whether the assets should be combined.
    """

    for linked_id_type, linked_id_values in linked_ids.items():
        link_table_name = f'dict__link_{linked_id_type}'
        linked_id_type = dictionary.link_table_name_to_id_type(link_table_name)

        for linked_id_value in linked_id_values:
            # should only be adding a linked_id if it doesnt already exist
                # if it already exists then we ignore it
            # should also check whether that id was associated with a different osuked asset
                # if a different asset is linked then we should unlink it

            # need to start linking these events to the users who carry them out
            # on startup should generate the linked id tables dynamically
                # should ensure that this works within the docker container

            db_client.create_record(
                {
                    'osuked_id': osuked_id,
                    linked_id_type: linked_id_value
                }, 
                link_table_name
            )

    return dictionary.load_site_ids(osuked_id, db_client)
