import pytest
from fastapi import status
from starlette.testclient import TestClient

from powerdict.api.main import app



@pytest.fixture
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture
def token(test_app):
    token = test_app.post(
        "authentication/token", data={"username": "ayrton", "password": "password"}
    )
    return token.json()["access_token"]


def test_get_docs(test_app, token):
    response = test_app.get('/docs')
    assert response.status_code == status.HTTP_200_OK


def test_get_hello(test_app, token):
    response = test_app.get(
        '/frictionless/hello',
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['msg'] == 'hello ayrton'
