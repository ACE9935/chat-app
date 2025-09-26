from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres@localhost:5432/postgres"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Use SQLModel as the Base
Base = SQLModel  

# Create a session factory
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
