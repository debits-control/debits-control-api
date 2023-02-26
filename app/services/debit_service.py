from app.repository.debit_repository import DebitRepository
from app.schema.debit_schema import DebitFormData, DebitCreate
from app.schema.user_schema import User
from app.services.base_service import BaseService


class DebitService(BaseService):
    def __init__(self, debit_repository: DebitRepository):
        super().__init__(debit_repository)

    def add_with_owner(self, debit_form_data: DebitFormData, user: User):
        payment_type_create = DebitCreate(
            **debit_form_data.dict(),
            user_id=user.id
        )
        return self.repository.create(payment_type_create)
