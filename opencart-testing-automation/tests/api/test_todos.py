import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert "completed" in todos[0]

@pytest.mark.api
def test_single_todo():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200
    todo = response.json()
    assert todo["id"] == 1
    assert "title" in todo
