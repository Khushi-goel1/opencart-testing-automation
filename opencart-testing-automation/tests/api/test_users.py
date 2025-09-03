import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert "name" in users[0]

@pytest.mark.api
def test_single_user_found():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "username" in user

@pytest.mark.api
def test_single_user_not_found():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404
