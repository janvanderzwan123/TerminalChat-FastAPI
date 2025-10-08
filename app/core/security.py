from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def truncate_password_to_72_bytes(password: str) -> str:
    """
    Truncate a password to 72 bytes safely without breaking UTF-8 characters.
    """
    encoded = password.encode("utf-8")
    if len(encoded) <= 72:
        return password
    # Truncate to 72 bytes safely
    truncated = encoded[:72]
    # Decode back to string ignoring incomplete UTF-8 sequences
    return truncated.decode("utf-8", errors="ignore")

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt safely truncated to 72 bytes.
    """
    safe_password = truncate_password_to_72_bytes(password)
    return pwd_context.hash(safe_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password against hashed password safely truncated to 72 bytes.
    """
    safe_password = truncate_password_to_72_bytes(plain_password)
    return pwd_context.verify(safe_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Alias for hash_password.
    """
    return hash_password(password)
