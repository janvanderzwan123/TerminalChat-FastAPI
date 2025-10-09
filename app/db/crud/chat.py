from sqlalchemy.orm import Session
from typing import List
from app.db.models.chat import Chat as ChatModel
from app.db.models.chat_members import ChatMember as ChatMemberModel
from app.schemas.chat import ChatCreate

def create_chat(db: Session, chat: ChatCreate):
    """
    Create a new chat in the database along with its members.
    """
    # Create SQLAlchemy Chat instance
    db_chat = ChatModel(name=chat.name, type=chat.type)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)

    # Add members
    for user_id in chat.members:
        db_member = ChatMemberModel(chat_id=db_chat.id, user_id=user_id)
        db.add(db_member)
    db.commit()
    db.refresh(db_chat)

    return db_chat

def get_chat(db: Session, chat_id: int):
    """
    Retrieve a single chat by ID.
    """
    return db.query(ChatModel).filter(ChatModel.id == chat_id).first()

def list_chats(db: Session):
    """
    Retrieve all chats.
    """
    return db.query(ChatModel).all()
