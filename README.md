# TK-LEARNING-AUTOMATION

[![Tests](https://github.com/tariksuid/LearningAutomation/actions/workflows/tests.yml/badge.svg)](https://github.com/tariksuid/LearningAutomation/actions/workflows/tests.yml)

A learning project for **API test automation** with **Python**, **pytest**, and **requests**.

The tests run against two practice APIs:

| API | What it's used for |
| --- | --- |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com) | Full **CRUD** (create, read, update, delete) on `/users`. It's a fake API that doesn't save changes, so POST, PUT, and DELETE tests check the response only. |
| [Restful-Booker](https://restful-booker.herokuapp.com) | Bookings that are **really saved**, plus **token authentication**. Tests verify the data by reading it back after each change. |

## Tech stack

- Python 3.14
- pytest — test framework
- requests — HTTP library for calling APIs
- GitHub Actions — CI that runs the tests on every push and pull request

## Project structure

```
TK-LEARNING-AUTOMATION/
├── .github/workflows/
│   └── tests.yml              # CI workflow: installs dependencies and runs pytest
├── tests/
│   ├── conftest.py            # shared fixtures (base URLs, auth token)
│   ├── test_bookings.py       # Restful-Booker: create and delete bookings
│   ├── test_create_user.py    # POST test for creating a user
│   ├── test_delete_user.py    # DELETE test for removing a user
│   ├── test_update_user.py    # PUT test for updating a user
│   └── test_users.py          # GET user tests with parametrize and boundary values
├── requirements.txt           # installed libraries and versions
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

```bash
source .venv/bin/activate
pytest -v
```

Run one file only:

```bash
pytest tests/test_users.py -v
```

## What the tests cover

### Restful-Booker

#### `test_bookings.py`

| Test | What it checks |
| --- | --- |
| `test_create_booking_is_saved` | a booking created with `POST /booking` can be read back with `GET` and has the same data |
| `test_delete_booking` | an authenticated `DELETE /booking/{id}` removes the booking, and `GET` then returns 404 |

Each test gets its own new booking from the `booking_id` fixture, so the tests don't depend on each other.

### JSONPlaceholder

#### `test_create_user.py`

| Test | What it checks |
| --- | --- |
| `test_create_user` | `POST /users` returns 201, a new `id`, and the same name, username, and email that were sent |

#### `test_delete_user.py`

| Test | What it checks |
| --- | --- |
| `test_delete_user` | `DELETE /users/1` returns 200 and an empty body (`{}`) |

#### `test_update_user.py`

| Test | What it checks |
| --- | --- |
| `test_update_user` | `PUT /users/1` returns 200, keeps the same `id`, and returns the updated name, username, and email |

#### `test_users.py`

| Test | What it checks |
| --- | --- |
| `test_get_valid_user` | first and last valid users (1 and 10) return 200, the correct `id`, a valid email, and a non-empty name (parametrized) |
| `test_missing_user_returns_404` | invalid users (0, 11, 9999) return 404 (negative, boundary test) |

## Testing practices used

- **Timeouts** on every request, so a slow server can't hang the test run
- **Status check before reading data**, for clear failure messages
- **Shared fixtures in `conftest.py`**: the API address lives in one place and every test file uses it
- **Parametrize** for data-driven testing: one test, many inputs
- **Positive and negative tests**: checking both success and error responses
- **Boundary value analysis**: testing the edges of valid data (1, 10) and just outside them (0, 11)
- **No redundant tests**: each test checks something no other test covers
- **Expected values from the test data**: POST checks compare the response to the data that was sent, not retyped values
- **Continuous integration**: every push and pull request runs the full suite on a fresh machine
- **Persistence checks**: after creating or deleting data, tests read it back to confirm the change was really saved
- **Authentication fixture**: `auth_token` logs in once per test and passes the token to tests that need it
- **Fixtures that create test data**: `booking_id` gives each test its own fresh booking, keeping tests independent
- **Documented code**: docstrings on fixtures and tests (shown by `pytest --fixtures`), and comments that explain API quirks
