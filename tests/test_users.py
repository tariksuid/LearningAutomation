import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def user():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    assert response.status_code == 200
    return response.json()


def test_user_id(user):
    assert user["id"] == 1


def test_user_has_email(user):
    assert "@" in user["email"]


@pytest.mark.parametrize("user_id", [1, 10])
def test_each_user_exists(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.parametrize("user_id", [0, 11, 9999])
def test_missing_user_returns_404(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
    assert response.status_code == 404
