from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr, scoped_session, Session

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class Database:
    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(
            database_url,
            connect_args={'check_same_thread': False},  # only needed to sqlite database, remove to others
            echo=True,
        )
        self._session_factory = scoped_session(
            sessionmaker(
                autoflush=False,
                autocommit=False,
                bind=self._engine
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    def get_db(self) -> Session:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
