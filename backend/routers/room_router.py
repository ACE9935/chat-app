from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from models import Message
from typing import List, Optional
from schemas import UserInfos
from services.room_service import get_room, create_room, get_users_in_room, room_exists, get_rooms_for_user
from database import get_db
from services.chat_service import get_messages_for_room

router = APIRouter(prefix="/v1/rooms", tags=["Rooms"])

@router.get("/{room_id}")
def read_room(room_id: str, db: Session = Depends(get_db)):
    room = get_room(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.get("/{user_id}/rooms")
def get_user_rooms(user_id: str, db: Session = Depends(get_db)):

    rooms = get_rooms_for_user(db, user_id)
    if not rooms:
        return []
    return rooms

@router.post("/")
def create_new_room(
    room_id: Optional[str] = Body(None),
    user_ids: List[str] = Body(...),
    db: Session = Depends(get_db),
):

    return create_room(db, room_id, user_ids)

# --- Get messages for a room ---
@router.get("/room/{room_id}", response_model=List[Message])
def get_room_messages(room_id: str, db: Session = Depends(get_db)):
    room = room_exists(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return get_messages_for_room(db, room_id)

@router.get("/{room_id}/users", response_model=List[UserInfos])
def get_room_users(room_id: str, db: Session = Depends(get_db)):
    users = get_users_in_room(db, room_id)
    if not users:
        raise HTTPException(status_code=404, detail="Room not found or no users in this room")
    return users