import uuid

def test_create_and_get_room(client):
    # Create a room
    response = client.post("/v1/rooms/", json=[])
    assert response.status_code == 200
    room_data = response.json()
    room_id = uuid.UUID(room_data["id"])  # convert string to UUID

    # Get the room
    response_get = client.get(f"/v1/rooms/{room_id}")
    assert response_get.status_code == 200

    # Get users in empty room → should 404
    response_users = client.get(f"/v1/rooms/{room_id}/users")
    assert response_users.status_code == 404
