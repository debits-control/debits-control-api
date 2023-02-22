from sqlalchemy import Column, Integer, String

from app.model.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    user_token = Column(String, unique=True)
