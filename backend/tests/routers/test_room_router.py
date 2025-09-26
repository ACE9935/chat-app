import uuid

def test_create_and_get_room(client):
    # Create a room
    room_id = uuid.uuid4() 

    response = client.post("/v1/rooms/", json={
        "user_ids": []
    })
    assert response.status_code == 200
    room_data = response.json()
    assert room_data["id"] == str(room_id)

    # Get the room
    response_get = client.get(f"/v1/rooms/{room_id}")
    assert response_get.status_code == 200
    assert response_get.json()["id"] == str(room_id)

    # Get users in empty room
    response_users = client.get(f"/v1/rooms/{room_id}/users")
    assert response_users.status_code == 404
