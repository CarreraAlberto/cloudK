# conexão e sessão com o PostgreSQL

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega variáveis de ../.env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# Monta string de conexão
URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Engine e sessão
engine = create_engine(URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
