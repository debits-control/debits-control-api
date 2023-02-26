from pydantic import BaseModel


class SignIn(BaseModel):
    email: str
    password: str


class SignInResponse(BaseModel):
    access_token: str


class SignUp(BaseModel):
    name: str
    email: str
    password: str


class Payload(BaseModel):
    id: int
    email: str
    name: str


class TokenPayload(Payload):
    exp: float
