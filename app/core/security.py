from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt, truncating to 72 bytes.
    """
    # truncate password to 72 characters (not bytes) for safety
    truncated = password[:72]
    return pwd_context.hash(truncated)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password against hashed password, truncating to 72 characters.
    """
    truncated = plain_password[:72]
    return pwd_context.verify(truncated, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Alias for hash_password.
    """
    return hash_password(password)
