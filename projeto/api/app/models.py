# definição das tabelas (SQLAlchemy)

from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id        = Column(Integer, primary_key=True, index=True)
    email     = Column(String, unique=True, index=True, nullable=False)
    hashed_pw = Column(String, nullable=False)
