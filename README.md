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
│   └── test_users.py    # user tests with fixtures and parametrize
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
| `test_user_id` | user 1 has the correct `id` |
| `test_user_has_email` | user 1's email contains `@` |
| `test_each_user_exists` | users 1–5 each return 200 and the correct `id` (parametrized) |
| `test_missing_user_returns_404` | a user that doesn't exist returns 404 (negative test) |

## Testing practices used

- **Timeouts** on every request, so a slow server can't hang the test run
- **Status check before reading data**, for clear failure messages
- **Fixtures** to share setup between tests (DRY: Don't Repeat Yourself)
- **Parametrize** for data-driven testing: one test, many inputs
- **Positive and negative tests**: checking both success and error responses
