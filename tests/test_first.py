import requests


def test_math_works():
    assert 2 + 2 == 4


def test_get_user_returns_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    assert response.status_code == 200


def test_user_has_expected_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "email" in user
    assert "name" in user
