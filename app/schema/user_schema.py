from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(ModelBaseInfo, UserBase):
    id: int
    user_token: str

    class Config:
        orm_mode = True
