import json
import logging

import pytest
from fastapi import status
from starlette.testclient import TestClient

from powerdict.api.main import app
from powerdict import frictionless, db, schemas


@pytest.fixture
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture
def token(test_app):
    token = test_app.post(
        "authentication/token", data={"username": "tester", "password": "password"}
    )
    return token.json()["access_token"]


@pytest.fixture
def example_data_package(
    fp: str = 'tests/data/repd-metadata.json'
):
    with open(fp, 'r') as f:
        data_package = json.load(f)

    if 'resources' in data_package.keys():
        for resource in data_package['resources']:
            if 'schema' in resource.keys():
                resource['fd_schema'] = resource.pop('schema')

    return data_package


def test_get_docs(test_app, token):
    response = test_app.get('/docs')
    assert response.status_code == status.HTTP_200_OK


def test_get_hello(test_app, token):
    response = test_app.get(
        '/frictionless/hello',
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['msg'] == 'hello tester'


def dict_deep_equals(d1, d2, path=""):
    for k in d1:
        if k in d2:
            if type(d1[k]) is dict:
                dict_deep_equals(d1[k], d2[k], "%s -> %s" % (path, k) if path else k)
            if d1[k] != d2[k]:
                result = ["%s: " % path, " - %s : %s" % (k, d1[k]), " + %s : %s" % (k, d2[k])]
                print("\n".join(result))
                return False
        else:
            print("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))
            return False

    return True

def test_data_package_roundtrip(test_app, token, example_data_package):
    # posting data package
    post_response = test_app.post(
        '/frictionless/data-packages',
        json=example_data_package,
        headers={'Authorization': f'Bearer {token}'},
    )

    assert post_response.status_code == status.HTTP_200_OK

    # retrieving data package
    data_package_id = post_response.json()

    get_response = test_app.get(
        f'/frictionless/data-packages/{data_package_id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert post_response.status_code == status.HTTP_200_OK

    # validating equality of input/output data packages
    loaded_record = get_response.json()
    loaded_record = schemas.DataPackage.parse_obj(loaded_record)
    loaded_record = db.db_record_to_dict_repr(loaded_record)

    assert dict_deep_equals(example_data_package, loaded_record)
