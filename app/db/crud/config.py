from sqlalchemy.orm import Session
from app.db.models.config import Config

def get_config_value(db: Session, key: str) -> str | None:
    config = db.query(Config).filter(Config.key == key).first()
    if config:
        return config.value
    return None

def get_all_configs(db: Session) -> dict:
    configs = db.query(Config).all()
    return {c.key: c.value for c in configs}

def set_config_value(db: Session, key: str, value: str) -> Config:
    config = db.query(Config).filter(Config.key == key).first()
    if config:
        config.value = value
    else:
        config = Config(key=key, value=value)
        db.add(config)
    db.commit()
    db.refresh(config)
    return config
