from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class PaymentTypeBase(BaseModel):
    name: str
    fee: float
    is_default: bool


class PaymentTypeCreate(PaymentTypeBase):
    ...


class PaymentType(ModelBaseInfo, PaymentTypeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
