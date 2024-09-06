from .conf_test import client

def test_login_for_access_token(client):
    response = client.post("/token", data={"username": "admin", "password": "adminadmin"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert "refresh_token" in response.json()

def test_get_users(client):
    response = client.post("/token", data={"username": "admin", "password": "adminadmin"})
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data

    token = response_data['access_token']
    response = client.get("/users/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

    users_data = response.json()
    assert isinstance(users_data, list)
