def test_get_users(client):
    # Create some users
    client.post("/v1/auth/signup", json={
        "email": "alice@example.com",
        "username": "alice",
        "password": "secret"
    })
    client.post("/v1/auth/signup", json={
        "email": "bob@example.com",
        "username": "bob",
        "password": "secret"
    })

    # Search users
    response = client.get("/v1/users/", params={"search": "alice"})
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["username"] == "alice"
