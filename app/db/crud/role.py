from sqlalchemy.orm import Session
from app.db.models.role import Role

def create_role(db: Session, name: str) -> Role:
    role = Role(name=name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def get_role(db: Session, role_id: int) -> Role:
    return db.query(Role).filter(Role.id == role_id).first()

def get_role_by_name(db: Session, name: str) -> Role:
    return db.query(Role).filter(Role.name == name).first()
