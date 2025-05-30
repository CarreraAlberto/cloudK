# funções de acesso ao banco e hashing de senha

from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, schemas

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # gera hash seguro com bcrypt + salt automático
    hashed = pwd_ctx.hash(user.senha)
    db_user = models.User(email=user.email, hashed_pw=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate(db: Session, email: str, senha: str):
    user = get_user_by_email(db, email)
    if not user or not pwd_ctx.verify(senha, user.hashed_pw):
        return None
    return user
