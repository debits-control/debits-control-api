from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.core.database import BaseModel


class Debit(BaseModel):
    __tablename__ = 'debits'

    name = Column(String)
    value = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    payment_type_id = Column(Integer, ForeignKey('payment_types.id'))
