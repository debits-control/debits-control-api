from sqlalchemy.orm import Session

from app.model.payment_type import PaymentType
from app.repository.base_repository import BaseRepository


class PaymentTypeRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, PaymentType)
