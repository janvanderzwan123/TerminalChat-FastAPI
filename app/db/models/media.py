from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from app.db.session import Base
from sqlalchemy.orm import relationship

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.id", ondelete="CASCADE"), nullable=False)
    media_type = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    message = relationship("Message", back_populates="media")
