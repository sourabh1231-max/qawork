import pytest
import requests
from jsonschema import validate, ValidationError

post_schema = {
    "type": "object",
    "required": ["userId","id","title","body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }
}

comment_schema = {
    "type": "object",
    "required": ["postId","id","name","email","body"],
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"}
    }
}

user_schema = {
    "type": "object",
    "required": ["id","name","username","email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    }
}

schema_map = {
    "/posts": (post_schema, True),
    "/comments": (comment_schema, True),
    "/users": (user_schema, True)
}

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_response_time_and_status(base_url, endpoint):
    url = base_url + endpoint
    resp = requests.get(url, timeout=10)
    # Status code should be 200
    assert resp.status_code == 200, f"Status code for {endpoint} was {resp.status_code}"
    # Response time < 2 seconds
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < 2, f"Response time too slow: {elapsed}s for {endpoint}"

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_schema_validation(base_url, endpoint):
    url = base_url + endpoint
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    schema, expect_list = schema_map[endpoint]
    # Validate first item (if list) or the object itself
    items = data if isinstance(data, list) else [data]
    assert len(items) > 0, f"No items returned for {endpoint}"
    for item in items[:5]:  # validate up to first 5 to keep test fast
        try:
            validate(instance=item, schema=schema)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed for {endpoint}: {e}")
