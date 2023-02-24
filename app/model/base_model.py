from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declared_attr, as_declarative


@as_declarative()
class BaseModel:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
