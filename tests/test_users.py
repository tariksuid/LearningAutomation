import pytest
import requests


@pytest.mark.parametrize("user_id", [1, 10])
def test_each_user_exists(user_id, base_url):
    response = requests.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert "@" in user["email"]


@pytest.mark.parametrize("user_id", [0, 11, 9999])
def test_missing_user_returns_404(user_id, base_url):
    response = requests.get(f"{base_url}/users/{user_id}", timeout=10)
    assert response.status_code == 404
