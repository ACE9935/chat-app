from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import UserInfos
from services.user_service import get_users_by_search, get_user_rooms
from database import get_db

router = APIRouter(prefix="/v1/users", tags=["Users"])

@router.get("/", response_model=List[UserInfos])
def get_users(search: str = "", db: Session = Depends(get_db)):
    return get_users_by_search(db, search)

@router.get("/{user_id}/rooms", response_model=List)
def get_rooms(user_id: str, db: Session = Depends(get_db)):
    rooms = get_user_rooms(db, user_id)
    if rooms is None:
        return []
    return rooms
