from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> User:
    """
    Get a user by username.
    """
    return db.query(User).filter(User.username == username).first()