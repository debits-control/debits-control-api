from sqlalchemy.orm import Session

from app.repository.payment_type_repository import PaymentTypeRepository
from app.services.payment_type_service import PaymentTypeService


def payment_type_factory(session: Session):
    repository = PaymentTypeRepository(session)
    return PaymentTypeService(repository)
