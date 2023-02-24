from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.debit import Debit
from app.repository.base_repository import BaseRepository


class DebitRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        super().__init__(session_factory, Debit)
