from sqlalchemy.orm import Session

from app.repository.user_repository import UserRepository
from app.services.user_service import UserService


def user_factory(session: Session):
    repository = UserRepository(session)
    return UserService(repository)
