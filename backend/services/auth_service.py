from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Converts a plain-text password into a secure hashed password.
    """
    return pwd_context.hash(password)