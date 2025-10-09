from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.role import Role
from app.core.security import get_password_hash  

def seed_admin(db: Session):
    admin_role = db.query(Role).filter(Role.name == "admin").first()
    if not admin_role:
        raise Exception("Admin role must exist before seeding admin user")

    existing_admin = db.query(User).filter(User.username == "admin").first()
    if not existing_admin:
        admin_user = User(
            name="Admin User",
            username="admin",
            email="janvanderzwan123@gmail.com",
            password=get_password_hash("Admin123"),  
            role_id=admin_role.id
        )
        db.add(admin_user)
        db.commit()
        print("Admin user seeded!")
    existing_test = db.query(User).filter(User.username == "test").first()
    if not existing_test:
        test_user = User(
            name="Test User",
            username="test",
            email="test@example.com",
            password=get_password_hash("Admin123"),  
            role_id=admin_role.id
        )
        db.add(test_user)
        db.commit()
        print("Test user seeded!")
