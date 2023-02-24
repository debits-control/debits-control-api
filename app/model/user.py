from sqlalchemy import Column, String

from app.core.database import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    user_token = Column(String, unique=True, nullable=True)
