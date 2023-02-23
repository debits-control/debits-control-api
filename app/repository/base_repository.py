from typing import Type

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import DuplicatedError, NotFoundError
from app.model.base_model import BaseModel
from app.schema.base_schema import BaseSchema


class BaseRepository:
    def __init__(self, session: Session, model: Type[BaseModel]):
        self.session = session
        self.model = model

    def read_list(self, skip: int, limit: int):
        return self.session.query(self.model).offset(skip).limit(limit).all()

    def read_by_id(self, id: int):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def create(self, schema: Type[BaseSchema]):
        query = self.model(**schema.dict())
        try:
            self.session.add(query)
            self.session.commit()
            self.session.refresh(query)
        except IntegrityError as e:
            raise DuplicatedError(detail=str(e.orig))
        return query

    def update(self, id: int, schema: Type[BaseSchema]):
        self.session\
            .query(self.model)\
            .filter(self.model.id == id)\
            .update(schema.dict(exclude_none=True))
        self.session.commit()
        return self.read_by_id(id)

    def update_attr(self, id: int, column: str, value):
        self.session\
            .query(self.model)\
            .filter(self.model.id == id)\
            .update({column: value})
        self.session.commit()
        return self.read_by_id(id)

    def delete_by_id(self, id: int):
        query = self.session.query(self.model).filter(self.model.id == id).first()
        if not query:
            raise NotFoundError(detail=f"not found id: {id}")
        self.session.delete(query)
        self.session.commit()
