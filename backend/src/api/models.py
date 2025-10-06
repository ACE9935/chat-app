from typing import Optional, List
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

# --- Link table for many-to-many between User and Room ---
class UserRoomLink(SQLModel, table=True):
    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    room_id: UUID = Field(foreign_key="room.id", primary_key=True)

# --- User model ---
class User(SQLModel, table=True):
    __tablename__ = "user"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    username: str = Field(unique=True, index=True, nullable=False)
    hashed_password: str

    rooms: List["Room"] = Relationship(back_populates="users", link_model=UserRoomLink)
    messages: List["Message"] = Relationship(back_populates="user")

    model_config = {
        "from_attributes": True  # Pydantic v2 replacement for orm_mode
    }

# --- Room model ---
class Room(SQLModel, table=True):
    __tablename__ = "room"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    users: List[User] = Relationship(back_populates="rooms", link_model=UserRoomLink)
    messages: List["Message"] = Relationship(back_populates="room")

    model_config = {
        "from_attributes": True
    }

# --- Message model ---
class Message(SQLModel, table=True):
    __tablename__ = "message"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    text: str
    user_id: UUID = Field(foreign_key="user.id")
    room_id: UUID = Field(foreign_key="room.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user: Optional[User] = Relationship(back_populates="messages")
    room: Optional[Room] = Relationship(back_populates="messages")

    model_config = {
        "from_attributes": True
    }
