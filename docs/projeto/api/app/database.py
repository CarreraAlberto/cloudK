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
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(base_dir, 'test.db')}"
)

# Constrói o engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        echo=True,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        DATABASE_URL,
        echo=True,
        future=True
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
