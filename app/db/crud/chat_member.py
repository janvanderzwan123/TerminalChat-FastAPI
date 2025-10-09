from sqlalchemy.orm import Session
from app.db.models import chat_members
from app.schemas.chat_member import ChatMemberCreate
from typing import List

def add_member(db: Session, member: ChatMemberCreate):
    db_member = chat_members(user_id=member.user_id, chat_id=member.chat_id)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def list_members(db: Session, chat_id: int) -> List[chat_members]:
    return db.query(chat_members).filter(chat_members.chat_id == chat_id).all()
