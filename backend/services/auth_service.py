from sqlalchemy.orm import Session
from models import User
from auth import get_password_hash, verify_password
from typing import Optional

def signup_user(db: Session, email: str, username: str, password: str) -> User:
    hashed_password = get_password_hash(password)
    new_user = User(email=email, username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(db: Session, email: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
