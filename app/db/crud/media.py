from sqlalchemy.orm import Session
from app.db.models import media
from app.schemas.media import MediaCreate
from typing import List

def add_media(db: Session, media: MediaCreate):
    db_media = media(message_id=media.message_id, file_url=media.file_url, media_type=media.media_type)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def get_media_for_message(db: Session, message_id: int) -> List[media]:
    return db.query(media).filter(media.message_id == message_id).all()
