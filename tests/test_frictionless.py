import json
import requests
import logging
import pytest
from powerdict import db, schemas, frictionless


def fd_metadata_from_url(fd_url: str):
    r = requests.get(fd_url)
    r.raise_for_status()
    return r.json()


def load_raw_fd_package(fd_fp):
    with open(fd_fp, 'r') as f:
        raw_fd_package = json.load(f)
        
    return raw_fd_package


def dict_deep_equals(d1, d2, path=""):
    for k in d1:
        if k in d2:
            if type(d1[k]) is dict:
                dict_deep_equals(d1[k], d2[k], "%s -> %s" % (path, k) if path else k)
            if d1[k] != d2[k]:
                result = [ "%s: " % path, " - %s : %s" % (k, d1[k]) , " + %s : %s" % (k, d2[k])]
                logging.warning("\n".join(result))
                return False
        else:
            logging.warning("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))
            return False
        
    return True


@pytest.mark.parametrize(
    'fd_fp', [
        pytest.param('tests/data/s-and-p-500-companies.json', id='s-and-p-500-companies'), 
        pytest.param('tests/data/repd-metadata.json', id='repd')
    ]
)
def test_fd_package_db_roundtrip(
    fd_fp: str
):
    # Fixed inputs
    db_fp = 'tests/data/dictionary.db'

    
    # DB initialisation
    db_client = db.DbClient(
        database_name=db_fp,
        dialect='sqlite',
        driver=None,
    )

    tables_to_create = [
        db.DataLicenseTable.__table__,
        db.DataContributorTable.__table__,
        db.DataSourceTable.__table__,
        db.FieldDescriptorTable.__table__,
        db.DataSchemaTable.__table__,
        db.DataResourceTable.__table__,
        db.DataPackageTable.__table__
    ]

    db_client.create_tables(tables_to_create)

    
    # Saving package to the DB
    raw_package_metadata = load_raw_fd_package(fd_fp)
    
    fd_package = frictionless.parse_fd_package_obj(raw_package_metadata, use_table_schemas=True)
    fd_package_id = fd_package.data_package_id
    db_records = frictionless.fd_package_to_db_records(fd_package)

    n_packages_in_db_before = len(db_client.get_all_data_packages())
    db_client.create_multi_table_records(db_records)
    n_packages_in_db_after = len(db_client.get_all_data_packages())

    assert (n_packages_in_db_after - n_packages_in_db_before) == 1, 'A new datapackage was not added to the DB'

    
    # Roundtrip validation
    fd_package_obj = db_client.get_data_package(fd_package_id, 'dict')
    fd_package_obj = schemas.DataPackage.parse_obj(fd_package_obj)
    fd_package_dict = db.db_record_to_dict_repr(fd_package_obj)
    
    for i, resource in enumerate(fd_package_dict['resources']):
        if 'fd_schema' in resource.keys():
            resource['schema'] = resource.pop('fd_schema')
    
    assert dict_deep_equals(fd_package_dict, load_raw_fd_package(fd_fp)), 'Failed roundtrip validation'
