from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum
from .chat_member import ChatMember
from .message import Message

class ChatType(str, Enum):
    PRIVATE = "private"
    GROUP = "group"

class ChatBase(BaseModel):
    type: ChatType
    name: Optional[str] = None

class ChatCreate(ChatBase):
    name: str 
    type: str
    members: Optional[list[int]] = []

class Chat(ChatBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    members: List[ChatMember] = []
    messages: List[Message] = []

    class Config:
        orm_mode = True

