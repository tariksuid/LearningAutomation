import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def booker_url():
    return "https://restful-booker.herokuapp.com"
