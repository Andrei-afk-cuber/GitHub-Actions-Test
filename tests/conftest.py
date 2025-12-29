import pytest

from app import app

@pytest.fixture
def response():
    return app.test_client().get('/')