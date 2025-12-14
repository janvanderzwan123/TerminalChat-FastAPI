from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.crud.user import create_user, get_user, get_all_users
from app.db.crud.role import get_role
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    role = get_role(db, user.role_id)
    if not role:
        raise HTTPException(status_code=400, detail="Role does not exist")
    
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=list[UserRead])
def read_all_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users