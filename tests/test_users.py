import pytest
from jose import jwt
from app import schemas
from .database import client,session
from app.config import settings

@pytest.fixture
def test_user(client):
    user_data = {
        "email": "sanjeev@gmail.com",
        "password": "password123"
    }
    res = client.post("/users/", json=user_data)
    
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

def test_create_user(client):
    payload = {"email": "hello123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=payload)
    
    assert res.status_code == 201

    new_user = UserOut(**res.json())
    assert new_user.email == payload["email"]

def test_login_user(test_user, client):
    res = client.post(
        "/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"]
        }
    )

    login_res = schemas.Token(**res.json())

    payload = jwt.decode(
        login_res.access_token,
        settings.secret_key,
        algorithms=[settings.algorithm]
    )

    id = payload.get("user_id")
    assert id == test_user["id"]
    assert res.status_code == 200

@pytest.mark.parametrize("email,password, status_code", [
    ('wrongemail@gamil.com', 'password123', 403),
    ('sanjeev@gmail.com','password123',403),
    ('wroungemail@gmail.com','wroungpassword',403),
])

def test_incorrect_login(test_user, client):
    res = client.post(
        "/login", data = {"username": test_user['email'],"password":"wrongPassword"})
    
    assert res.status_code == 403
    assert res.json().get('detail') == 'Invalide Credentials'