from app.repository.payment_type_repository import PaymentTypeRepository
from app.schema.payment_type_schema import PaymentTypeCreate, PaymentTypeFormData
from app.schema.user_schema import User
from app.services.base_service import BaseService


class PaymentTypeService(BaseService):
    def __init__(self, payment_type_repository: PaymentTypeRepository):
        super().__init__(payment_type_repository)

    def add_with_owner(self, payment_type_form_data: PaymentTypeFormData, user: User):
        payment_type_create = PaymentTypeCreate(
            **payment_type_form_data.dict(),
            owner_id=user.id
        )
        return self.repository.create(payment_type_create)
