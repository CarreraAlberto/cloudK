# modelos Pydantic (entrada e saída)

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    senha: str

class Token(BaseModel):
    jwt: str



# chat, to estudando aqui tudo isso que voce ta falando e 
# vou tirar algumas duvidas com voce. 
# # 1 - em schemas.py, posso escrever o que a mesma classe necessita
# # de resposta sem referenciar duas vezes? ou seja:
# class UserBase(BaseModel):
#     email: EmailStr
#     senha : str

#     é a mesma coisa que 

# class UserBase(BaseModel):
#     email: EmailStr

# class UserCreate(UserBase):
#     senha: str