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
    linked_ids: dict[str, list],
    db_client: db.DbClient
):
    linked_data = {}

    for source_link in source_links:
        if source_link['linked_id_type'] not in linked_data.keys():
            linked_data[source_link['linked_id_type']] = {}

        records = db_client.get_all(source_link['resource_table_name'], flat_table=True)
        print(records[0])

        linked_data[source_link['linked_id_type']][source_link['data_resource_id']] = {
            record[source_link['linked_id_column']]: record
            for record 
            in records
            if record[source_link['linked_id_column']] in linked_ids[source_link['linked_id_type']]
        }

    return linked_data

def load_site_data(
    osuked_id: int,
    db_client: db.DbClient,
    source_links: list[schemas.SourceLink]
):
    linked_ids = get_linked_ids(osuked_id, db_client)
    linked_data = get_linked_data(source_links, linked_ids, db_client)

    return {
        'osuked_id': osuked_id, 
        'linked_ids': linked_ids,
        'linked_data': linked_data
    }
