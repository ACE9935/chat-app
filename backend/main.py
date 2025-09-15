from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, List, Tuple

app = FastAPI()

class PrivateChatManager:
    def __init__(self):
        # rooms = { room_id: [WebSocket1, WebSocket2] }
        self.rooms: Dict[str, List[WebSocket]] = {}

    def get_room_id(self, user1: str, user2: str) -> str:
        """Generate a unique room ID for two users"""
        return "_".join(sorted([user1, user2]))

    async def connect(self, room_id: str, websocket: WebSocket):
        """Add a user's WebSocket to a room"""
        await websocket.accept()
        if room_id not in self.rooms:
            self.rooms[room_id] = []
        self.rooms[room_id].append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        """Remove a user's WebSocket from a room"""
        if room_id in self.rooms:
            self.rooms[room_id].remove(websocket)
            if not self.rooms[room_id]:
                del self.rooms[room_id]

    async def send_message(self, room_id: str, message: str):
        """Send a message to all sockets in a room"""
        if room_id in self.rooms:
            for connection in self.rooms[room_id]:
                await connection.send_text(message)


chat_manager = PrivateChatManager()


@app.websocket("/ws/{user1}/{user2}/{username}")
async def websocket_endpoint(websocket: WebSocket, user1: str, user2: str, username: str):
    room_id = chat_manager.get_room_id(user1, user2)
    await chat_manager.connect(room_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await chat_manager.send_message(room_id, f"{username}: {data}")
    except WebSocketDisconnect:
        chat_manager.disconnect(room_id, websocket)
        await chat_manager.send_message(room_id, f"⚠️ {username} left the chat")
