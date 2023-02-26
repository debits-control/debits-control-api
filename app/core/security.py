from datetime import datetime, timedelta

from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from passlib.context import CryptContext

from app.core.exceptions import ForbiddenError, AuthError
from app.core.settings import settings

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
ALGORITHM = 'HS256'


def get_hashed_password(password: str):
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_context.verify(password, hashed_password)


def create_access_token(subject: dict, expires_delta: timedelta = None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {'exp': expires_delta, **subject}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, ALGORITHM)
    return encoded_jwt


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, ALGORITHM)
        return decoded_token if decoded_token['exp'] > int(round(datetime.utcnow().timestamp())) else None
    except ():
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise ForbiddenError(detail='Invalid authentication scheme.')
            if not self.verify_jwt(credentials.credentials):
                raise AuthError(detail='Invalid token or expired token.')
            return credentials.credentials
        else:
            raise AuthError(detail='Invalid authorization token.')

    @staticmethod
    def verify_jwt(jwt_token: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = decode_jwt(jwt_token)
        except ():
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid
