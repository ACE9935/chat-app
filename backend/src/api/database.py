import os
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.environ.get("DB_URL")

engine = create_engine(DB_URL, echo=True)

Base = SQLModel
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

