# from fastapi.testclient import TestClient
# from ..app.main import app

# client = TestClient(app)

# def test_get_users():
#     response = client.post("/token", data={"username": "admin", "password": "adminadmin"})
#     assert response.status_code == 200
#     response_data = response.json()
#     assert "access_token" in response_data

#     token = response_data['access_token']
#     response = client.get("/users/", headers={"Authorization": f"Bearer {token}"})
#     assert response.status_code == 200

#     users_data = response.json()
#     assert isinstance(users_data, list)
