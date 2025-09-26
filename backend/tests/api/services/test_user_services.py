from unittest.mock import MagicMock

from backend.src.api.models import User
from unittest.mock import MagicMock
from backend.src.api.services.user_service import get_user_rooms, get_users_by_search
from backend.src.api.models import User

def test_get_users_by_search_returns_limited_users():
    # GIVEN
    db = MagicMock()
    query = MagicMock()
    db.query.return_value = query
    filter_result = MagicMock()
    query.filter.return_value = filter_result
    filter_result.limit.return_value.all.return_value = ["user1", "user2"]

    # WHEN
    result = get_users_by_search(db, search="abc", limit=2)

    # THEN
    assert result == ["user1", "user2"]
    db.query.assert_called_once_with(User)
    query.filter.assert_called_once()
    filter_result.limit.assert_called_once_with(2)
    filter_result.limit.return_value.all.assert_called_once()


def test_get_user_rooms_returns_rooms_for_existing_user():
    # GIVEN
    db = MagicMock()
    rooms = ["room1", "room2"]
    user = MagicMock()
    user.rooms = rooms
    query = MagicMock()
    query.filter.return_value.first.return_value = user
    db.query.return_value = query

    # WHEN
    result = get_user_rooms(db, user_id="123")

    # THEN
    assert result == rooms
    db.query.assert_called_once_with(User)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()

def test_get_user_rooms_returns_none_if_user_not_found():
    # GIVEN
    db = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = None
    db.query.return_value = query

    # WHEN
    result = get_user_rooms(db, user_id="123")

    # THEN
    assert result is None
    db.query.assert_called_once_with(User)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()
