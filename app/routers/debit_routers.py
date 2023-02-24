from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.debit_schema import Debit
from app.services.debit_service import DebitService

debit_router = APIRouter(
    prefix='/debit',
    tags=['debit']
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
