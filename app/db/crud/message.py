from sqlalchemy.orm import Session
from app.db.models import message
from app.schemas.message import MessageCreate
from typing import List

def create_message(db: Session, msg: MessageCreate):
    db_msg = message(chat_id=msg.chat_id, sender_id=msg.sender_id, content=msg.content)
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg

def get_messages(db: Session, chat_id: int) -> List[message]:
    return db.query(message).filter(message.chat_id == chat_id).order_by(message.timestamp).all()
