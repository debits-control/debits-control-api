from pydantic import BaseModel


class SignUp(BaseModel):
    name: str
    email: str
    password: str


class SignInResponse(BaseModel):
    access_token: str


class Payload(BaseModel):
    id: int
    email: str
    name: str


class TokenPayload(Payload):
    exp: float
