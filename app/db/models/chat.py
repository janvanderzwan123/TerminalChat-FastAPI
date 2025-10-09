from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from app.db.session import Base
from sqlalchemy.orm import relationship
import enum

class ChatType(str, enum.Enum):
    PRIVATE = "private"
    GROUP = "group"

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(ChatType), nullable=False)
    name = Column(String(255), nullable=True)  # length added
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    members = relationship("ChatMember", back_populates="chat", cascade="all, delete-orphan")
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
