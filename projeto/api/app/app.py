# onde os endpoints são definidos

import os
from fastapi import FastAPI, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from . import models, schemas, crud, auth, external
from .database import SessionLocal, engine, Base

import socket
from datetime import datetime, timezone

# Carrega .env e cria tabelas
load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud API")


# # Dependência para obter o token Bearer
# bearer_scheme = HTTPBearer()

# Dependência para obter sessão do DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registrar", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(409, "Email já cadastrado")
    crud.create_user(db, user)
    token = auth.create_token(user.email)
    return {"jwt": token}

@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.authenticate(db, user.email, user.senha)
    if not db_user:
        raise HTTPException(401, "Credenciais inválidas")
    token = auth.create_token(user.email)
    return {"jwt": token}

@app.get("/consultar")
def consultar(authorization: str = Header(...), db: Session = Depends(get_db)):
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(403, "Token de autenticação inválido")
    try:
        email = auth.verify_token(token)
    except ValueError:
        raise HTTPException(403, "Token inválido ou expirado")
    # opcional: checar se o usuário ainda existe
    if not crud.get_user_by_email(db, email):
        raise HTTPException(403, "Usuário não encontrado")
    return external.fetch_data()
# def consultar(
#     credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
#     db: Session = Depends(get_db),
# ):
#     token = credentials.credentials                # o JWT puro
#     try:
#         email = auth.verify_token(token)
#     except ValueError:
#         raise HTTPException(status.HTTP_403_FORBIDDEN, "Token inválido ou expirado")
#     if not crud.get_user_by_email(db, email):
#         raise HTTPException(status.HTTP_403_FORBIDDEN, "Usuário não encontrado")
#     return external.fetch_data()



@app.get("/health_check")
def health_check():
    return {
        "statusCode": 200,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "hostname": socket.gethostname()
    }