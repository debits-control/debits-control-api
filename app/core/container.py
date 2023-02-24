from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton, Factory

from app.core.database import Database
from app.core.settings import settings
from app.repository.payment_type_repository import PaymentTypeRepository
from app.repository.user_repository import UserRepository
from app.services.user_service import UserService


class Container(DeclarativeContainer):

    wiring_config = WiringConfiguration(
        modules=[
            'app.routers.user_routers',
            'app.routers.payment_type_routers'
        ]
    )

    database = Singleton(Database, database_url=settings.DATABASE_URL)

    user_repository = Factory(UserRepository, session_factory=database.provided.session)
    payment_type_repository = Factory(PaymentTypeRepository, session_factory=database.provided.session)

    user_service = Factory(UserService, user_repository=user_repository)
    payment_type_service = Factory(PaymentTypeRepository, payment_type_repository=payment_type_repository)
