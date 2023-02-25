from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

from app.core.settings import settings

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='signin'
)


def get_hashed_password(password: str):
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_context.verify(password, hashed_password)


def create_access_token(subject: dict, expires_delta: timedelta = None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {'exp': expires_delta, 'sub': str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, ALGORITHM)
    return encoded_jwt
