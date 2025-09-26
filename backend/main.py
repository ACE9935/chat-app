from fastapi import FastAPI
from sqlmodel import SQLModel
from backend.database import engine
from backend.routers import auth_router, user_router, room_router, chat_router
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(bind=engine)
    print("Tables created!")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# ---- Add CORS ----
origins = [
    "http://localhost:5173",  # Vite/React dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Routers ----
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(room_router.router)
app.include_router(chat_router.router)
