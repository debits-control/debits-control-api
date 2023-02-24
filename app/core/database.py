from typing import Any

from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr, Session

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},  # only needed to sqlite database, remove to others
    echo=True,
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def get_db() -> Session:
    session: Session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


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
        self.session_local = sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=self._engine
        )

    def create_database(self) -> None:
        BaseModel.metadata.create_all(self._engine)

    def get_db(self) -> Session:
        session: Session = self.session_local()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
