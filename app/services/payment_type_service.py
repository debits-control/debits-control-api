from app.repository.payment_type_repository import PaymentTypeRepository
from app.services.base_service import BaseService


class PaymentTypeService(BaseService):
    def __init__(self, payment_type_repository: PaymentTypeRepository):
        super().__init__(payment_type_repository)
