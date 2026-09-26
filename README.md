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
│   ├── test_first.py    # basic API checks
│   └── test_users.py    # user tests with parametrize and boundary values
├── requirements.txt     # installed libraries and versions
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

### `test_first.py`

| Test | What it checks |
| --- | --- |
| `test_math_works` | pytest is set up correctly |
| `test_get_user_returns_200` | `GET /users/1` returns status 200 (OK) |
| `test_user_has_expected_fields` | user 1 has `id`, `name`, and `email` fields |

### `test_users.py`

| Test | What it checks |
| --- | --- |
| `test_each_user_exists` | first and last valid users (1 and 10) return 200, the correct `id`, and a valid email (parametrized) |
| `test_missing_user_returns_404` | invalid users (0, 11, 9999) return 404 (negative, boundary test) |

## Testing practices used

- **Timeouts** on every request, so a slow server can't hang the test run
- **Status check before reading data**, for clear failure messages
- **Parametrize** for data-driven testing: one test, many inputs
- **Positive and negative tests**: checking both success and error responses
- **Boundary value analysis**: testing the edges of valid data (1, 10) and just outside them (0, 11)
- **No redundant tests**: each test checks something no other test covers
