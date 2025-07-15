
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_student():
    # Create
    resp = client.post("/students", json={
        "name": "Alice",
        "age": 20,
        "email": "alice@example.com"
    })
    assert resp.status_code == 201
    student = resp.json()
    assert student["name"] == "Alice"

    # Duplicate email should fail
    dup_resp = client.post("/students", json={
        "name": "Bob",
        "age": 22,
        "email": "alice@example.com"
    })
    assert dup_resp.status_code == 400

    # Retrieve
    sid = student["id"]
    resp2 = client.get(f"/students/{sid}")
    assert resp2.status_code == 200
    assert resp2.json()["email"] == "alice@example.com"
