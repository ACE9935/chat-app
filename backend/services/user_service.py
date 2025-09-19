from sqlalchemy.orm import Session
from models import User, Room

def get_users_by_search(db: Session, search: str, limit: int = 5):
    return db.query(User).filter(User.username.ilike(f"%{search}%")).limit(limit).all()

def get_user_rooms(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    return user.rooms
