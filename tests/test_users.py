import pytest
import requests


@pytest.mark.parametrize("user_id", [1, 10])
def test_get_valid_user(user_id, jsonplaceholder_url):
    response = requests.get(f"{jsonplaceholder_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert "@" in user["email"]
    assert user["name"]


@pytest.mark.parametrize("user_id", [0, 11, 9999])
def test_missing_user_returns_404(user_id, jsonplaceholder_url):
    response = requests.get(f"{jsonplaceholder_url}/users/{user_id}", timeout=10)
    assert response.status_code == 404
