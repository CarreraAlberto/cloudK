# modelos Pydantic (entrada e saída)

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    senha: str

class Token(BaseModel):
    jwt: str



