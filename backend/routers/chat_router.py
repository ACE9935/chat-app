from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlmodel import Session
from typing import Dict, List
from services.chat_service import save_message, get_messages_for_room
from database import get_db
from uuid import UUID

router = APIRouter()

# Track active WebSocket connections per room
active_connections: Dict[UUID, List[WebSocket]] = {}

@router.websocket("/ws/private/{room_id}")
async def websocket_chat(
    room_id: UUID,
    websocket: WebSocket,
    db: Session = Depends(get_db)
):
    await websocket.accept()

    if room_id not in active_connections:
        active_connections[room_id] = []

    active_connections[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            user_id = UUID(data["user_id"])
            text = data["text"]

            # Save message to DB
            message = save_message(db, text=text, user_id=user_id, room_id=room_id)

            # Broadcast to all connected clients in this room
            for connection in active_connections[room_id]:
                await connection.send_json({
                    "id": str(message.id),
                    "text": message.text,
                    "user_id": str(message.user_id),
                    "room_id": str(message.room_id),
                    "created_at": message.created_at.isoformat()
                })

    except WebSocketDisconnect:
        active_connections[room_id].remove(websocket)
