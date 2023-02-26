from pydantic import BaseModel

from app.schema.base_schema import BaseSchema


class PaymentTypeBase(BaseModel):
    name: str
    fee: float
    is_default: bool


class PaymentTypeFormData(PaymentTypeBase):
    ...


class PaymentTypeCreate(PaymentTypeBase):
    owner_id: int


class PaymentType(BaseSchema, PaymentTypeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
