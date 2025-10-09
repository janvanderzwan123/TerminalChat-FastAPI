from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.crud import chat_member as crud
from app.db.base import get_db
from app.schemas.chat_member import ChatMember, ChatMemberCreate
from typing import List

router = APIRouter(prefix="/chat-members", tags=["Chat Members"])



@router.post("/", response_model=ChatMember)
def add_chat_member(member: ChatMemberCreate, db: Session = Depends(get_db)):
    return crud.add_member(db, member)

@router.get("/{chat_id}", response_model=List[ChatMember])
def list_chat_members(chat_id: int, db: Session = Depends(get_db)):
    return crud.list_members(db, chat_id)

#dit is een comment