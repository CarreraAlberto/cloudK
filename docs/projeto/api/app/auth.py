# criação e validação do token JWT

import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

SECRET = os.getenv("JWT_SECRET")
ALGO   = os.getenv("JWT_ALGO", "HS256")
EXP    = int(os.getenv("JWT_EXPIRY_MIN", "60"))

def create_token(subject: str) -> str:
    now = datetime.utcnow()
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(minutes=EXP)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        return payload.get("sub")
    except JWTError as e:
        raise ValueError("Token inválido ou expirado") from e


