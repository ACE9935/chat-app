import pytest
from unittest.mock import MagicMock
from backend.services.auth_service import login_user, signup_user
from backend.models import User  

def test_signup_user_creates_user_and_saves_to_db(mocker):
    # GIVEN
    db = MagicMock()
    email = "test@example.com"
    username = "testuser"
    password = "secret"

    mock_hash = mocker.patch("backend.services.auth_service.get_password_hash", return_value="hashed123")

    # WHEN
    user = signup_user(db, email=email, username=username, password=password)

    # THEN
    mock_hash.assert_called_once_with(password)
    db.add.assert_called_once_with(user)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(user)
    assert isinstance(user, User)
    assert user.email == email
    assert user.username == username
    assert user.hashed_password == "hashed123"

def test_login_user_returns_none_if_user_not_found(mocker):
    # GIVEN
    db = MagicMock()
    query = MagicMock()
    query.filter.return_value.first.return_value = None 
    db.query.return_value = query

    # WHEN
    result = login_user(db, email="ghost@example.com", password="secret")

    # THEN
    db.query.assert_called_once_with(User)
    query.filter.assert_called_once()
    query.filter.return_value.first.assert_called_once()
    assert result is None
