from app.core.database import Database, SQLALCHEMY_DATABASE_URL
from app.repository.user_repository import UserRepository
from app.services.user_service import UserService


class Container:

    database = Database(database_url=SQLALCHEMY_DATABASE_URL)
    # session = database.get_db()
    user_repository = UserRepository(session=database.get_db())
    user_service = UserService(user_repository=user_repository)
