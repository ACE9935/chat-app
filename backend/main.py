from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routers import auth_router, user_router, room_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(bind=engine)
    print("Tables created!")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(room_router.router)
