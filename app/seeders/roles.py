from sqlalchemy.orm import Session
from app.db.models.role import Role

def seed_roles(db: Session):
    roles = ["admin", "user"]
    for role_name in roles:
        existing_role = db.query(Role).filter(Role.name == role_name).first()
        if not existing_role:
            role = Role(name=role_name)
            db.add(role)
    db.commit()
    print("Roles seeded!")
