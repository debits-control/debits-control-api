from contextlib import AbstractContextManager
from typing import Type, Callable

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import BaseModel
from app.core.exceptions import DuplicatedError, NotFoundError


class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], model: Type[BaseModel]):
        self.session_factory = session_factory
        self.model = model

    def read_list(self, skip: int, limit: int):
        with self.session_factory() as session:
            return session.query(self.model).offset(skip).limit(limit).all()

    def read_by_id(self, id: int):
        with self.session_factory() as session:
            return session.query(self.model).filter(self.model.id == id).first()

    def create(self, schema):
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return query

    def update(self, id: int, schema):
        with self.session_factory() as session:
            session\
                .query(self.model)\
                .filter(self.model.id == id)\
                .update(schema.dict(exclude_none=True))
            session.commit()
            return self.read_by_id(id)

    def update_attr(self, id: int, column: str, value):
        with self.session_factory() as session:
            session\
                .query(self.model)\
                .filter(self.model.id == id)\
                .update({column: value})
            session.commit()
            return self.read_by_id(id)

    def delete_by_id(self, id: int):
        with self.session_factory() as session:
            query = session.query(self.model).filter(self.model.id == id).first()
            if not query:
                raise NotFoundError(detail=f"not found id: {id}")
            session.delete(query)
            session.commit()
