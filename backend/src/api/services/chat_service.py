from sqlalchemy.orm import Session
from ..models import Message
from typing import List

def save_message(db: Session, text: str, user_id: str, room_id: str) -> Message:
    new_message = Message(text=text, user_id=user_id, room_id=room_id)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_messages_for_room(db: Session, room_id: str) -> List[Message]:
    return db.query(Message).filter(Message.room_id == room_id).order_by(Message.created_at).all()

