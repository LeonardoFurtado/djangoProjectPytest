import pytest
from rest_framework.test import APIClient
from core.models import Profile


@pytest.fixture
def api_client():
    client = APIClient()
    headers = {"HTTP_AUTHORIZATION": f"Token Teste"}
    client.credentials(**headers)
    return client


@pytest.fixture
def create_user(mocker):
    return mocker.patch("core.auth.get_auth_context", return_value=3)
