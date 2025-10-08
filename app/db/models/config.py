from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(191), unique=True, nullable=False)  
    value = Column(String(255), nullable=False)