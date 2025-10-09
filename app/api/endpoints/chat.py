from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.crud import chat as crud_chat
from app.db.base import get_db
from app.schemas.chat import Chat, ChatCreate

router = APIRouter(prefix="/chats", tags=["Chats"])


@router.post("/", response_model=Chat)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    if not chat.members:
        raise HTTPException(status_code=400, detail="Chat must have at least one member")
    return crud_chat.create_chat(db, chat)

@router.get("/{chat_id}", response_model=Chat)
def read_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = crud_chat.get_chat(db, chat_id)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat

@router.get("/", response_model=list[Chat])
def list_all_chats(db: Session = Depends(get_db)):
    return crud_chat.list_chats(db)
