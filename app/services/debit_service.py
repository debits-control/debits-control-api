from app.repository.debit_repository import DebitRepository
from app.services.base_service import BaseService


class DebitService(BaseService):
    def __init__(self, debit_repository: DebitRepository):
        super().__init__(debit_repository)
