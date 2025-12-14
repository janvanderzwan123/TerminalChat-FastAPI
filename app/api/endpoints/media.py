from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.crud import media as crud
from app.db.base import get_db
from app.schemas.media import Media, MediaCreate
from typing import List

router = APIRouter(prefix="/media", tags=["Media"])


@router.post("/", response_model=Media)
def upload_media(media: MediaCreate, db: Session = Depends(get_db)):
    return crud.add_media(db, media)

@router.get("/{message_id}", response_model=List[Media])
def get_media(message_id: int, db: Session = Depends(get_db)):
    return crud.get_media_for_message(db, message_id)
