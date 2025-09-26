import uuid
from sqlalchemy.orm import Session
from backend.models import Room, User, UserRoomLink
from typing import List, Optional

def get_room(db: Session, room_id: str):
    return db.query(Room).filter(Room.id == room_id).first()

def create_room(db: Session, user_ids: List[str]):

    room = Room()
    db.add(room)
    db.refresh(room) 

    for user_id in user_ids:
        # avoid duplicates
        if not db.query(UserRoomLink).filter_by(user_id=user_id, room_id=room.id).first():
            db.add(UserRoomLink(user_id=user_id, room_id=room.id))

    db.commit()
    db.refresh(room) 

    return room

def room_exists(db: Session, room_id: str) -> bool:
    return db.query(Room).filter(Room.id == room_id).first()

def get_rooms_for_user(db: Session, user_id: str) -> List[Room]:
 
    return (
        db.query(Room)
        .join(UserRoomLink, Room.id == UserRoomLink.room_id)
        .filter(UserRoomLink.user_id == user_id)
        .all()
    )

def get_users_in_room(db: Session, room_id: str) -> List[User]:
    
    users = (
        db.query(User)
        .join(UserRoomLink, User.id == UserRoomLink.user_id)
        .filter(UserRoomLink.room_id == room_id)
        .all()
    )
    return users
