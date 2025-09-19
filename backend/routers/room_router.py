from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from models import Message
from typing import List
from schemas import MessageCreate
from services.room_service import get_room, create_room, room_exists
from database import get_db
from services.message_service import get_messages_for_room, save_message
from auth import decode_access_token

router = APIRouter(prefix="/v1/rooms", tags=["Rooms"])

@router.get("/{room_id}")
def read_room(room_id: str, db: Session = Depends(get_db)):
    room = get_room(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.post("/")
def create_new_room(
    room_id: str = Body(...),
    user_ids: List[str] = Body(...),
    db: Session = Depends(get_db),
    token: str = None
):
    user_data = decode_access_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    all_users = [user_data["user_id"]] + user_ids
    return create_room(db, room_id, all_users)

@router.post("/{room_id}/messages")
def post_message(
    room_id: str,
    message: MessageCreate,
    db: Session = Depends(get_db),
    token: str = None
):
    user_data = decode_access_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    return save_message(db, message.text, user_data["user_id"], room_id)

# --- Get messages for a room ---
@router.get("/room/{room_id}", response_model=List[Message])
def get_room_messages(room_id: str, db: Session = Depends(get_db)):
    room = room_exists(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return get_messages_for_room(db, room_id)
