import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE
