import uuid
from unittest.mock import MagicMock, ANY
from backend.src.api.services.room_service import (
    get_room,
    create_room,
    room_exists,
    get_rooms_for_user,
    get_users_in_room
)
from backend.src.api.models import Room, User, UserRoomLink


def test_get_room_returns_room_if_exists():
    db = MagicMock()
    room_id = uuid.uuid4()
    room = Room(id=room_id)

    query = MagicMock()
    query.filter.return_value.first.return_value = room
    db.query.return_value = query

    result = get_room(db, str(room_id))  # pass as string

    assert result == room
    db.query.assert_called_once_with(Room)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()


def test_create_room_creates_room_and_user_links():
    db = MagicMock()
    db.query.return_value.filter_by.return_value.first.return_value = None
    user_ids = [str(uuid.uuid4()), str(uuid.uuid4())]  # valid UUID strings

    room = Room(id=uuid.uuid4())
    
    # Only set id if object is Room
    def add_side_effect(obj):
        if isinstance(obj, Room):
            obj.id = room.id

    db.add.side_effect = add_side_effect
    db.commit.side_effect = lambda: None
    db.refresh.side_effect = lambda x: None

    result = create_room(db, user_ids)

    assert db.add.call_count == 1 + len(user_ids)
    db.commit.assert_called()
    db.refresh.assert_called()
    assert isinstance(result.id, uuid.UUID)


def test_room_exists_returns_true_if_room_found():
    db = MagicMock()
    query = MagicMock()
    room_id = uuid.uuid4()
    query.filter.return_value.first.return_value = Room(id=room_id)
    db.query.return_value = query

    result = room_exists(db, str(room_id))

    assert result is True
    db.query.assert_called_once_with(Room)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()


def test_room_exists_returns_false_if_room_not_found():
    db = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = None
    db.query.return_value = query

    result = room_exists(db, str(uuid.uuid4()))
    assert result is False


def test_get_rooms_for_user_returns_rooms():
    db = MagicMock()
    rooms = [Room(id=uuid.uuid4()), Room(id=uuid.uuid4())]
    query = MagicMock()
    query.join.return_value.filter.return_value.all.return_value = rooms
    db.query.return_value = query

    result = get_rooms_for_user(db, str(uuid.uuid4()))

    assert result == rooms
    db.query.assert_called_once_with(Room)
    query.join.assert_called_once_with(UserRoomLink, ANY)
    query.join.return_value.filter.assert_called_once()
    query.join.return_value.filter.return_value.all.assert_called_once()


def test_get_users_in_room_returns_users():
    db = MagicMock()
    users = [User(id=uuid.uuid4()), User(id=uuid.uuid4())]
    query = MagicMock()
    query.join.return_value.filter.return_value.all.return_value = users
    db.query.return_value = query

    result = get_users_in_room(db, str(uuid.uuid4()))

    assert result == users
    db.query.assert_called_once_with(User)
    query.join.assert_called_once_with(UserRoomLink, ANY)
    query.join.return_value.filter.assert_called_once()
    query.join.return_value.filter.return_value.all.assert_called_once()
