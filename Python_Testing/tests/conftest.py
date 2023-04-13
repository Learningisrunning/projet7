import pytest

from server import app

@pytest.fixture
def created_app():

    created_app = app
    
    yield created_app

@pytest.fixture
def client(created_app):
    return created_app.test_client()

        