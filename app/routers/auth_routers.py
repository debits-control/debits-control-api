from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.auth_schema import SignInResponse, SignUp, SignIn
from app.schema.user_schema import User
from app.services.auth_service import AuthService

auth_router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)


@auth_router.post('/sign-in', response_model=SignInResponse)
@inject
async def sign_in(
        sign_in_data: SignIn,
        service: AuthService = Depends(Provide[Container.auth_service])
):
    return service.sign_in(sign_in_data)


@auth_router.post('/sign-up', response_model=User)
@inject
async def sign_in(
        user_info: SignUp,
        service: AuthService = Depends(Provide[Container.auth_service])
):
    return service.sign_up(user_info)
