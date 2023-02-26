from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.security import JWTBearer
from app.schema.user_schema import User, UserCreate
from app.services.user_service import UserService

router = APIRouter(
    prefix='/user',
    tags=['user'],
    dependencies=[Depends(JWTBearer())],
)


@router.get('', response_model=list[User])
@inject
async def get_user_list(
        service: UserService = Depends(Provide[Container.user_service])
):
    return service.get_list()


@router.post('', response_model=User)
@inject
async def create_user(
        user: UserCreate,
        service: UserService = Depends(Provide[Container.user_service])
):
    return service.add(user)


@router.post('/{user_id}', response_model=User)
@inject
async def get_user_by_id(
        user_id: int,
        service: UserService = Depends(Provide[Container.user_service])
):
    return service.get_by_id(user_id)
