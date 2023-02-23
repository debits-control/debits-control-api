from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.factory.payment_type_factory import payment_type_factory
from app.schema.payment_type_schema import PaymentType

payment_type_router = APIRouter(
    prefix='/payment-type',
    tags=['payment-type']
)


@payment_type_router.get('', response_model=list[PaymentType])
async def get_payment_type_list(
        session: Session = Depends(get_db)
):
    service = payment_type_factory(session)
    return service.get_list()