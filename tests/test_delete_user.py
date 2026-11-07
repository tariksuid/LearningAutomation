import pytest
import requests


@pytest.mark.parametrize("user_id", [1])
def test_delete_user(jsonplaceholder_url, user_id):
    response = requests.delete(f"{jsonplaceholder_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    assert response.json() == {}
