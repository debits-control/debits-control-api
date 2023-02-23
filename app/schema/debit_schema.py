from pydantic import BaseModel

from app.schema.base_schema import BaseSchema


class DebitBase(BaseModel):
    name: str
    value: float


class DebitCreate(DebitBase):
    ...


class Debit(BaseSchema, DebitBase):
    id: int
    user_id: int
    payment_type_id: int

    class Config:
        orm_mode = True
