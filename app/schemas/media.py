from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl

class MediaBase(BaseModel):
    media_type: str
    url: HttpUrl

class MediaCreate(MediaBase):
    pass

class Media(MediaBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
