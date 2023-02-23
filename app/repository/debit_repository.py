from sqlalchemy.orm import Session

from app.model.debit import Debit
from app.repository.base_repository import BaseRepository


class DebitRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Debit)
