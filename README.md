# TK-LEARNING-AUTOMATION

A learning project for **API test automation** with **Python**, **pytest**, and **requests**.

The tests run against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake REST API for practice.

## Tech stack

- Python 3.14
- pytest — test framework
- requests — HTTP library for calling APIs

## Project structure

```
TK-LEARNING-AUTOMATION/
├── tests/
│   ├── conftest.py            # shared fixtures (base_url)
│   ├── test_create_user.py    # POST test for creating a user
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

### `test_create_user.py`

| Test | What it checks |
| --- | --- |
| `test_create_user` | `POST /users` returns 201, a new `id`, and the same name, username, and email that were sent |

> JSONPlaceholder is a fake API: it returns a created user but doesn't save it, so the test checks the response only.

### `test_update_user.py`

| Test | What it checks |
| --- | --- |
| `test_update_user` | `PUT /users/1` returns 200, keeps the same `id`, and returns the updated name, username, and email |

### `test_users.py`

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
