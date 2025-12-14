from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.crud import message as crud
from app.db.base import get_db
from app.schemas.message import Message, MessageCreate
from typing import List

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("/", response_model=Message)
def send_message(msg: MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, msg)

@router.get("/{chat_id}", response_model=List[Message])
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    return crud.get_messages(db, chat_id)
