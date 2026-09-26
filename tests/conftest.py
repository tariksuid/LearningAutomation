import pytest
import requests


# Fixtures in this file are available to every test file in tests/
# without an import. pytest matches them by name.


@pytest.fixture
def base_url():
    """Base URL of JSONPlaceholder, a fake API that doesn't save changes."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def booker_url():
    """Base URL of Restful-Booker, a practice API that saves data for real."""
    return "https://restful-booker.herokuapp.com"


@pytest.fixture
def auth_token(booker_url):
    """Log in to Restful-Booker and return an auth token."""
    # Public demo credentials from the Restful-Booker docs.
    # Real credentials belong in environment variables, never in code.
    credentials = {"username": "admin", "password": "password123"}
    response = requests.post(f"{booker_url}/auth", json=credentials, timeout=10)
    assert response.status_code == 200
    return response.json()["token"]
