from pydantic import BaseModel

from app.schema.base_schema import BaseSchema


class PaymentTypeBase(BaseModel):
    name: str
    fee: float
    is_default: bool


class PaymentTypeCreate(PaymentTypeBase):
    ...


class PaymentType(BaseSchema, PaymentTypeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
