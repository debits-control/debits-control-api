from datetime import datetime

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from jose import jwt
from pydantic import ValidationError

from app.core.container import Container
from app.core.exceptions import AuthError, ForbiddenError
from app.core.security import oauth2_scheme, ALGORITHM
from app.core.settings import settings
from app.schema.auth_schema import TokenPayload
from app.schema.user_schema import User
from app.services.user_service import UserService


@inject
async def get_current_user(
        token: str = Depends(oauth2_scheme),
        service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    try:
        decoded_token_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_payload = TokenPayload(**decoded_token_payload)
        if datetime.fromtimestamp(token_payload.exp) < datetime.now():
            raise AuthError(detail='Token expired.')
    except (jwt.JWTError, ValidationError):
        raise ForbiddenError(detail='Could not validate credentials')
    current_user = service.get_by_id(token_payload.id)
    if not current_user:
        raise AuthError(detail='User not found')
    return current_user
