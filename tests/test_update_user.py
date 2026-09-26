import pytest
import requests


@pytest.mark.parametrize("user_id", [1])
def test_update_user(base_url, user_id):
    updated_user = {
        "name": "Sherlock Holmes",
        "username": "sherlock",
        "email": "sherlock@example.com",
    }
    response = requests.put(f"{base_url}/users/{user_id}", json=updated_user, timeout=10)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert user["name"] == updated_user["name"]
    assert user["username"] == updated_user["username"]
    assert user["email"] == updated_user["email"]
