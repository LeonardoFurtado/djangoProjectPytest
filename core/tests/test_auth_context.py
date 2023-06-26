import pytest


@pytest.mark.django_db
def test_create_profile(api_client, create_user):
    data = {
        "name": "Naruto Uzumaki",
    }
    response = api_client.post('/profiles/', data=data)
    assert response.status_code == 200

