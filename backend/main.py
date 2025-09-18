from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User
from schemas import UserCreate, UserLogin, Token
from auth import verify_password, get_password_hash, create_access_token, decode_access_token
from typing import List

Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # React dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for all origins (not safe for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Auth routes ---
@app.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(new_user.id, new_user.username, new_user.email)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(db_user.id, db_user.username, db_user.email)
    return {"access_token": token, "token_type": "bearer"}

# --- Global chat manager ---
class ChatManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for conn in self.connections:
            await conn.send_text(message)

chat_manager = ChatManager()

# --- WebSocket with JWT auth ---
@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket, token: str):
    user = decode_access_token(token)
    if not user:
        await websocket.close(code=1008)
        return

    username = user["username"]
    user_id = user["user_id"]

    await chat_manager.connect(websocket)
    await chat_manager.broadcast(f"⚡ {username} joined the chat")

    try:
        while True:
            data = await websocket.receive_text()
            await chat_manager.broadcast(f"{username}: {data} (id: {user_id})")
    except WebSocketDisconnect:
        chat_manager.disconnect(websocket)
        await chat_manager.broadcast(f"⚠️ {username} left the chat")

