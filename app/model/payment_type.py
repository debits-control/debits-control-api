from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, func

from app.core.database import Base


class PaymentType(Base):
    __tablename__ = 'payment_types'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(String)
    fee = Column(Float)
    is_default = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))
