from unittest.mock import MagicMock, ANY
from backend.services.room_service import get_room, create_room, room_exists, get_rooms_for_user, get_users_in_room
from backend.models import Room, User, UserRoomLink

def test_get_room_returns_room_if_exists():
    # GIVEN
    db = MagicMock()
    room = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = room
    db.query.return_value = query

    # WHEN
    result = get_room(db, "room_id")

    # THEN
    assert result == room
    db.query.assert_called_once_with(Room)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()

def test_create_room_creates_room_and_user_links():
    # GIVEN
    db = MagicMock()
    db.query.return_value.filter_by.return_value.first.return_value = None  
    user_ids = ["user1", "user2"]

    # WHEN
    room = create_room(db, room_id=None, user_ids=user_ids)

    assert db.add.call_count == 1 + len(user_ids)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(room)
    assert isinstance(room.id, str)

def test_room_exists_returns_true_if_room_found():
    # GIVEN
    db = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = MagicMock()  # room exists
    db.query.return_value = query

    # WHEN
    result = room_exists(db, "room_id")

    # THEN
    assert result is not None
    db.query.assert_called_once_with(Room)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()

def test_room_exists_returns_false_if_room_not_found():
    # GIVEN
    db = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = None  # no room
    db.query.return_value = query

    # WHEN
    result = room_exists(db, "room_id")

    # THEN
    assert result is None

def test_get_rooms_for_user_returns_rooms():
    # GIVEN
    db = MagicMock()
    rooms = ["room1", "room2"]
    query = MagicMock()
    query.join.return_value.filter.return_value.all.return_value = rooms
    db.query.return_value = query

    # WHEN
    result = get_rooms_for_user(db, "user1")

    # THEN
    assert result == rooms
    db.query.assert_called_once_with(Room)
    query.join.assert_called_once_with(UserRoomLink, ANY)
    query.join.return_value.filter.assert_called_once()
    query.join.return_value.filter.return_value.all.assert_called_once()

def test_get_users_in_room_returns_users():
    # GIVEN
    db = MagicMock()
    users = ["user1", "user2"]
    query = MagicMock()
    query.join.return_value.filter.return_value.all.return_value = users
    db.query.return_value = query

    # WHEN
    result = get_users_in_room(db, "room1")

    # THEN
    assert result == users
    db.query.assert_called_once_with(User)
    query.join.assert_called_once_with(UserRoomLink, ANY)
    query.join.return_value.filter.assert_called_once()
    query.join.return_value.filter.return_value.all.assert_called_once()
