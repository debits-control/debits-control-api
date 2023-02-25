from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.payment_type_schema import PaymentType
from app.services.payment_type_service import PaymentTypeService

payment_type_router = APIRouter(
    prefix='/payment-type',
    tags=['payment-type']
)


@payment_type_router.get('', response_model=list[PaymentType])
@inject
async def get_payment_type_list(
        service: PaymentTypeService = Depends(Provide[Container.payment_type_service])
):
    return service.get_list()


@payment_type_router.get('/{payment_type_id}', response_model=PaymentType)
@inject
async def get_payment_type_by_id(
        payment_type_id: int,
        service: PaymentTypeService = Depends(Provide[Container.payment_type_service])
):
    return service.get_by_id(payment_type_id)
