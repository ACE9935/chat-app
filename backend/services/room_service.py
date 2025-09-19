from sqlalchemy.orm import Session
from models import Room, UserRoomLink
from typing import List

def get_room(db: Session, room_id: str):
    return db.query(Room).filter(Room.id == room_id).first()

def create_room(db: Session, room_id: str, user_ids: List[str]):
    new_room = Room(id=room_id)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)

    for u_id in user_ids:
        link = UserRoomLink(user_id=u_id, room_id=new_room.id)
        db.add(link)
    db.commit()
    db.refresh(new_room)
    return new_room

def room_exists(db: Session, room_id: str) -> bool:
    return db.query(Room).filter(Room.id == room_id).first()