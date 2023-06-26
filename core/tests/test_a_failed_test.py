import pytest

@pytest.mark.django_db
def test_random_test(api_client):
    """
    If you comment this test, the test on file test_auth_context will pass
    """
    response = api_client.patch(
        '/route/that_doesnt_exists/',
        format='json'
    )
    assert response.status_code == 200
