from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInfos(BaseModel):
    id: UUID
    username: str
    email: str

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    text: str