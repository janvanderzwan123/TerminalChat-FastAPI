from sqlalchemy.orm import Session
from .roles import seed_roles
from .users import seed_admin
from app.db.session import SessionLocal

def run_seeders():
    db: Session = SessionLocal()
    try:
        seed_roles(db)
        seed_admin(db)
    finally:
        db.close()

if __name__ == "__main__":
    run_seeders()
    print("All seeders executed!")
