from pydantic import BaseModel

from app.schema.base_schema import BaseSchema


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(BaseSchema, UserBase):
    id: int

    class Config:
        orm_mode = True
