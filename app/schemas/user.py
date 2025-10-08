from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.role import RoleRead

class UserBase(BaseModel):
    name: str
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role_id: int

class UserRead(UserBase):
    id: int
    role: RoleRead

    class Config:
        orm_mode = True
