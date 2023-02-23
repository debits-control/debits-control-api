from sqlalchemy import Column, String, Integer, DateTime, func

from app.core.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    user_token = Column(String, unique=True, nullable=True)
