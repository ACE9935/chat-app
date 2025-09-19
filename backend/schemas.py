from pydantic import BaseModel, EmailStr

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
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    text: str