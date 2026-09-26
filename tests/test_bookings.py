import pytest
import requests


# Test data shared by every test in this file.
# UPPERCASE means it's a constant: tests read it but never change it.
NEW_BOOKING = {
    "firstname": "Sherlock",
    "lastname": "Holmes",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-10-01",
        "checkout": "2026-10-05",
    },
    "additionalneeds": "Breakfast",
}


@pytest.fixture
def booking_id(booker_url):
    """Create a new booking and return its id.

    Runs again for every test that asks for it, so each test gets its own booking.
    """
    response = requests.post(f"{booker_url}/booking", json=NEW_BOOKING, timeout=10)
    # Restful-Booker returns 200 for a create, not the usual 201.
    assert response.status_code == 200
    created_booking = response.json()
    return created_booking["bookingid"]


def test_create_booking_is_saved(booker_url, booking_id):
    """A created booking can be read back with the same data."""
    response_get = requests.get(f"{booker_url}/booking/{booking_id}", timeout=10)
    assert response_get.status_code == 200
    saved_booking = response_get.json()
    assert saved_booking["firstname"] == NEW_BOOKING["firstname"]
    assert saved_booking["lastname"] == NEW_BOOKING["lastname"]


def test_delete_booking(booker_url, auth_token, booking_id):
    """A deleted booking can no longer be found."""
    # Precondition: the booking exists before we delete it.
    response_get = requests.get(f"{booker_url}/booking/{booking_id}", timeout=10)
    assert response_get.status_code == 200

    # Restful-Booker expects the auth token as a cookie.
    headers = {"Cookie": f"token={auth_token}"}
    response_delete = requests.delete(f"{booker_url}/booking/{booking_id}", headers=headers, timeout=10)
    # Restful-Booker returns 201 for a delete (a known quirk of this API).
    assert response_delete.status_code == 201

    # The booking is really gone.
    response_get = requests.get(f"{booker_url}/booking/{booking_id}", timeout=10)
    assert response_get.status_code == 404
