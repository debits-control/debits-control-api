from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr, Session, scoped_session


@as_declarative()
class BaseModel:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


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
        BaseModel.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
