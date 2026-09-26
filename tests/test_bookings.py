import requests


def test_create_booking_is_saved(booker_url):
    new_booking = {
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
    response = requests.post(f"{booker_url}/booking", json=new_booking, timeout=10)
    assert response.status_code == 200
    created_booking = response.json()
    booking_id = created_booking["bookingid"]
    response_get = requests.get(f"{booker_url}/booking/{booking_id}", timeout=10)
    assert response_get.status_code == 200
    saved_booking = response_get.json()
    assert saved_booking["firstname"] == new_booking["firstname"]
    assert saved_booking["lastname"] == new_booking["lastname"]
