import uuid
from sqlalchemy.orm import Session
from ..models import Room, User, UserRoomLink
from typing import List

def get_room(db: Session, room_id: str):
    room_uuid = uuid.UUID(room_id)
    return db.query(Room).filter(Room.id == room_uuid).first()

def create_room(db: Session, user_ids: List[str]):
    room = Room()
    db.add(room)
    db.commit()
    db.refresh(room)

    for user_id in user_ids:
        user_uuid = uuid.UUID(user_id)
        if not db.query(UserRoomLink).filter_by(user_id=user_uuid, room_id=room.id).first():
            db.add(UserRoomLink(user_id=user_uuid, room_id=room.id))

    db.commit()
    db.refresh(room)
    return room

def room_exists(db: Session, room_id: str) -> bool:
    room_uuid = uuid.UUID(room_id)
    return db.query(Room).filter(Room.id == room_uuid).first() is not None

def get_rooms_for_user(db: Session, user_id: str) -> List[Room]:
    user_uuid = uuid.UUID(user_id)
    return (
        db.query(Room)
        .join(UserRoomLink, Room.id == UserRoomLink.room_id)
        .filter(UserRoomLink.user_id == user_uuid)
        .all()
    )

def get_users_in_room(db: Session, room_id: str) -> List[User]:
    room_uuid = uuid.UUID(room_id)
    return (
        db.query(User)
        .join(UserRoomLink, User.id == UserRoomLink.user_id)
        .filter(UserRoomLink.room_id == room_uuid)
        .all()
    )
