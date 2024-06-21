from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_login_for_access_token():
    response = client.post("/token", data={"username": "admin", "password": "adminadmin"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert "refresh_token" in response.json()