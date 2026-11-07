import requests


def test_create_user(jsonplaceholder_url):
    new_user = {
        "name": "Sherlock Holmes",
        "username": "sherlock",
        "email": "sherlock.holmes@example.com",
    }
    response = requests.post(f"{jsonplaceholder_url}/users", json=new_user, timeout=10)
    assert response.status_code == 201
    user = response.json()
    assert user["id"] is not None
    assert user["name"] == new_user["name"]
    assert user["username"] == new_user["username"]
    assert user["email"] == new_user["email"]
