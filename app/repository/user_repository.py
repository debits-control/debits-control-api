from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from app.model.user import User
from app.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        super().__init__(session_factory, User)
