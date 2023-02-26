from pydantic import BaseModel

from app.schema.base_schema import BaseSchema


class DebitBase(BaseModel):
    name: str
    value: float
    payment_type_id: int


class DebitFormData(DebitBase):
    ...


class DebitCreate(DebitBase):
    user_id: int


class Debit(BaseSchema, DebitBase):
    id: int

    class Config:
        orm_mode = True
