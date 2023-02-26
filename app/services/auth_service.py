from datetime import timedelta

from app.core.exceptions import AuthError
from app.core.security import verify_password, create_access_token, get_hashed_password
from app.core.settings import settings
from app.repository.user_repository import UserRepository
from app.schema.auth_schema import Payload, SignInResponse, SignUp, SignIn
from app.schema.user_schema import UserCreate
from app.services.base_service import BaseService


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def sign_in(self, sign_in_data: SignIn):
        user = self.user_repository.ready_by_email(sign_in_data.email)
        if not user:
            raise AuthError(detail='Incorrect username or password')
        if not verify_password(sign_in_data.password, user.password):
            raise AuthError(detail='Incorrect username or password')

        payload = Payload(
            id=user.id,
            email=user.email,
            name=user.name,
        )

        token_lifespan = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(subject=payload.dict(), expires_delta=token_lifespan)
        sign_in_result = SignInResponse(
            access_token=access_token
        )
        return sign_in_result

    def sign_up(self, user_info: SignUp):
        found_user = self.user_repository.ready_by_email(user_info.email)
        if found_user:
            raise AuthError(detail='A user with this email already exists.')
        user = UserCreate(**user_info.dict())
        user.password = get_hashed_password(user_info.password)
        created_user = self.user_repository.create(user)
        delattr(created_user, 'password')
        return created_user
