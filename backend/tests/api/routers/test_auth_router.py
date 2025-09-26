def test_signup_login(client):
    # Signup a new user
    response = client.post("/v1/auth/signup", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "secret"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

    # Try to login with wrong password
    response_fail = client.post("/v1/auth/login", json={
        "email": "test@example.com",
        "password": "wrong"
    })
    assert response_fail.status_code == 400

    # Login with correct password
    response_login = client.post("/v1/auth/login", json={
        "email": "test@example.com",
        "password": "secret"
    })
    assert response_login.status_code == 200
    assert "access_token" in response_login.json()
