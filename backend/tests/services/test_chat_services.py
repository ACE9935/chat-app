import pytest
from unittest.mock import MagicMock
from backend.services.chat_service import save_message, get_messages_for_room
from backend.models import Message

def test_save_message_adds_commits_and_refreshes():
    # GIVEN
    db = MagicMock()
    text = "Hello"
    user_id = "user1"
    room_id = "room1"

    # WHEN
    message = save_message(db, text=text, user_id=user_id, room_id=room_id)

    # THEN
    db.add.assert_called_once_with(message)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(message)
    assert isinstance(message, Message)
    assert message.text == text
    assert message.user_id == user_id
    assert message.room_id == room_id

def test_get_messages_for_room_returns_ordered_messages():
    # GIVEN
    db = MagicMock()
    messages = [MagicMock(), MagicMock()]  
    query = MagicMock()
    query.filter.return_value.order_by.return_value.all.return_value = messages
    db.query.return_value = query
    room_id = "room1"

    # WHEN
    result = get_messages_for_room(db, room_id)

    # THEN
    assert result == messages
    db.query.assert_called_once_with(Message)
    query.filter.assert_called_once()
    query.filter.return_value.order_by.assert_called_once()
    query.filter.return_value.order_by.return_value.all.assert_called_once()
