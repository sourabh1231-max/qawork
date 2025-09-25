#!/usr/bin/env python3
"""api_script.py

Task 1:
- Fetch all posts from https://jsonplaceholder.typicode.com/posts
- Validate status code == 200
- Verify each post contains keys: userId, id, title, body
- Save first 5 posts into posts_first_5.json
"""
import requests
import sys
import json

API = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    resp = requests.get(API, timeout=10)
    print(f"Status code: {resp.status_code}")
    if resp.status_code != 200:
        raise SystemExit(f"Unexpected status code: {resp.status_code}")
    posts = resp.json()
    # Validate structure
    required_keys = {"userId", "id", "title", "body"}
    for i, p in enumerate(posts):
        if not required_keys.issubset(p.keys()):
            raise ValueError(f"Post at index {i} missing keys. Found: {list(p.keys())}")
    # Save first 5
    with open("posts_first_5.json", "w", encoding="utf-8") as fh:
        json.dump(posts[:5], fh, indent=2)
    print("Saved first 5 posts to posts_first_5.json")

if __name__ == '__main__':
    fetch_posts()
