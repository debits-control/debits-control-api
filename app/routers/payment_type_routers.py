from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependency import get_current_user
from app.core.security import oauth2_scheme
from app.schema.payment_type_schema import PaymentType, PaymentTypeFormData
from app.schema.user_schema import User
from app.services.payment_type_service import PaymentTypeService

payment_type_router = APIRouter(
    prefix='/payment-type',
    tags=['payment-type'],
    dependencies=[Depends(oauth2_scheme)],
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


@payment_type_router.post('', response_model=PaymentType)
@inject
async def create_payment_type(
        payment_type_form_data: PaymentTypeFormData,
        service: PaymentTypeService = Depends(Provide[Container.payment_type_service]),
        current_user: User = Depends(get_current_user),
):
    return service.add_with_owner(payment_type_form_data, current_user)
