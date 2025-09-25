# QA Automation Package

This package contains solutions for multiple QA automation tasks:

## Contents
- `api_script.py` — Script to fetch posts from JSONPlaceholder, validate, and save first 5.
- `tests/` — Pytest suite with:
  - Response time validation (<2s)
  - Schema validation using `jsonschema`
  - Parameterized endpoints: `/posts`, `/comments`, `/users`
- `postman_collection.json` — Postman collection with tests for GET, POST, DELETE.
- `playwright_test.py` — Playwright script for UI automation on Rahul Shetty Academy Practice page.
- `strategy_and_leadership.txt` — Short answers for QA leadership and strategy.
- `requirements.txt` — Install all Python dependencies.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Task 1: Run API Script
```bash
python api_script.py
```
This saves the first 5 posts to `posts_first_5.json`.

## Task 2: Run Pytest Suite with Reports
### Basic run:
```bash
pytest -v
```

### Generate JUnit XML report:
```bash
pytest -v --junitxml=report.xml
```

### Generate HTML report (requires `pytest-html`):
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

## Task 3: Postman
Import `postman_collection.json` into Postman and run requests with included tests.

## Task 4: Playwright
Install browsers:
```bash
playwright install
```
Run test:
```bash
pytest -q playwright_test.py
```

## Task 5: Strategy & Leadership
Read `strategy_and_leadership.txt`.

---

### Notes
- Ensure you have internet access for API tests (jsonplaceholder.typicode.com).
- For CI/CD, integrate pytest with `--junitxml` or `--html` options for reporting.
# qawork
