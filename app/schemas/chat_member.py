from datetime import datetime
from pydantic import BaseModel

class ChatMemberBase(BaseModel):
    user_id: int

class ChatMemberCreate(ChatMemberBase):
    chat_id: int

class ChatMember(ChatMemberBase):
    id: int
    chat_id: int
    joined_at: datetime

    class Config:
        orm_mode = True
