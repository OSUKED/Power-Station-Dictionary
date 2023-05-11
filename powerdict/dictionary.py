from typing import Any
from powerdict import db, schemas


def get_linked_ids(
    osuked_id: int,
    db_client: db.DbClient,
    link_tables: list[str] = [
        'dict__link_repd',
        'dict__link_bmu',
    ]
):
    linked_ids = {}

    for link_table in link_tables:
        linked_id_col = link_table.split('_')[-1] + '_id'
        linked_ids[link_table] = [record[linked_id_col] for record in db_client.get_all(link_table) if record['osuked_id'] == osuked_id]

    return linked_ids

def get_linked_data(
    source_links: list,
    linked_ids: dict[Any, list],
    db_client: db.DbClient
):
    # should group linked_ids under linked_id_type then list sources separately 

    linked_data = {}

    for source_link in source_links:
        if source_link['linked_id_type'] not in linked_data.keys():
            linked_data[source_link['linked_id_type']] = {}

        records = db_client.get_all(source_link['resource_table_name'], flat_table=True)

        linked_data[source_link['linked_id_type']][source_link['resource_table_name']] = {
            record[source_link['linked_id_column']]: {
                k: v
                for k, v
                in record.items()
                if v is not None
            }
            for record 
            in records
            if record[source_link['linked_id_column']] in linked_ids[source_link['linked_id_type']]
        }

    return linked_data

def load_site_ids(
    osuked_id: int,
    db_client: db.DbClient
):
    linked_ids = get_linked_ids(osuked_id, db_client)
    
    return {
        'osuked_id': osuked_id, 
        'linked_ids': linked_ids
    }

def load_site_data(
    osuked_id: int,
    db_client: db.DbClient,
    source_links: list[schemas.SourceLink]
):
    site_data = load_site_ids(osuked_id, db_client)

    site_data.update({
        'linked_data': get_linked_data(source_links, site_data['linked_ids'], db_client)
    })
    
    return site_data

def link_table_name_to_id_type(
    link_table_name: str
):        
    link_table_schema = db.table_name_to_schema[link_table_name]

    linked_id_types = list(set(link_table_schema.schema()['properties'].keys()) - set(['osuked_id', 'date_added', 'date_removed']))
    assert len(linked_id_types) == 1, f'Expected 1 linked id attribute to be returned, instead got: {linked_id_types}'
    linked_id_type = linked_id_types[0]

    return linked_id_type