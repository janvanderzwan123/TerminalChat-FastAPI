from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .media import Media, MediaCreate

class MessageBase(BaseModel):
    content: Optional[str] = None

class MessageCreate(MessageBase):
    chat_id: int
    sender_id: int
    media: Optional[List[MediaCreate]] = []

class Message(MessageBase):
    id: int
    chat_id: int
    sender_id: int
    created_at: datetime
    media: List[Media] = []

    class Config:
        orm_mode = True
