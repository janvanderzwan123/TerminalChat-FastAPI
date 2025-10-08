from pydantic_settings import BaseSettings
from pydantic import AnyUrl
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.crud.config import get_all_configs

class Settings(BaseSettings):
    DATABASE_URL: AnyUrl

    APP_NAME: str = "FastAPI App"
    DEBUG: bool = True
    SECRET_KEY: str = "supersecret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

def load_db_config(settings: Settings):
    db: Session = SessionLocal()
    try:
        configs = get_all_configs(db)
    finally:
        db.close()

    for key, value in configs.items():
        if hasattr(settings, key):
            attr_type = type(getattr(settings, key))
            if attr_type is bool:
                value = value.lower() in ("true", "1", "yes")
            elif attr_type is int:
                value = int(value)
            setattr(settings, key, value)

load_db_config(settings)
