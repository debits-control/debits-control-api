from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependency import get_current_user
from app.core.security import oauth2_scheme
from app.schema.debit_schema import Debit, DebitFormData
from app.schema.user_schema import User
from app.services.debit_service import DebitService

debit_router = APIRouter(
    prefix='/debit',
    tags=['debit'],
    dependencies=[Depends(oauth2_scheme)]
)


@debit_router.get('', response_model=list[Debit])
@inject
async def get_debit_list(
        service: DebitService = Depends(Provide[Container.debit_service])
):
    return service.get_list()


@debit_router.get('/{debit_id}', response_model=Debit)
@inject
async def get_debit_by_id(
        debit_id: int,
        service: DebitService = Depends(Provide[Container.debit_service])
):
    return service.get_by_id(debit_id)


@debit_router.post('', response_model=Debit)
@inject
async def create_debit(
        debit_form_data: DebitFormData,
        service: DebitService = Depends(Provide[Container.debit_service]),
        current_user: User = Depends(get_current_user),
):
    return service.add_with_owner(debit_form_data, current_user)
