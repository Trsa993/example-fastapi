import pytest
from jose import jwt
from app import schemas
from app.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# def test_root(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "hello world!"}


def test_create_user(client):
    response = client.post("/users/", json={"email": "konj@email.com", "password":"12345"})
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "konj@email.com"
    assert response.status_code == 201
    

def test_login_user(client, test_user):
    response = client.post("/login", data={"username": test_user["email"], "password":test_user["password"]})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, SECRET_KEY, algorithms=ALGORITHM)
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_response.token_type == "bearer"
    assert response.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@mail.com", "12345", 403),
    ("konj@email.com", "qwerty", 403),
    ("wrongemail@mail.com", "qwerty", 403),
    (None, "12345", 422),
    ("konj@email.com", None, 422)
])
def test_incorrect_login(client, email, password, status_code):
    response = client.post("/login", data={"username": email, "password": password})
    assert response.status_code == status_code
    # assert response.json().get("detail") == "Invalid Credentials"
