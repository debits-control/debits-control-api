from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, func

from app.core.database import BaseModel


class PaymentType(BaseModel):
    __tablename__ = 'payment_types'

    name = Column(String)
    fee = Column(Float)
    is_default = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))
