# # conexão e sessão com o PostgreSQL

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega .env (com JWT e POSTGRES_ e, opcional, DATABASE_URL)
base_dir = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(base_dir, "../.env"))

# Se estiver em Docker, definimos DATABASE_URL no .env
# Caso contrário, cairá no fallback para SQLite local
        # DATABASE_URL = (f"postgresql://admin_user:cloudkcloudk@ls-d873d07a9a75b5d56df773e94247e024341049f4.c8hqgu8egqfy.us-east-1.rds.amazonaws.com:5432/dbfastapi")


user = os.getenv("POSTGRES_USER")
pwd  = os.getenv("POSTGRES_PASSWORD")
db   = os.getenv("POSTGRES_DB")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT", "5432")

DATABASE_URL = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"


# Constrói o engine de conexão com o banco de dados
engine = create_engine(
        DATABASE_URL,
        echo=True,
        future=True
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
