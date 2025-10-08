# app/db/base.py
from .session import SessionLocal

def get_db():
    """
    Dependency for FastAPI routes.
    Yields a SQLAlchemy session and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
