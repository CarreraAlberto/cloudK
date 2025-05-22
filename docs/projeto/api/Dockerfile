# 1. Base image
FROM python:3.11-slim

# 2. Define diretório de trabalho
WORKDIR /app

# 3. Copia_requirements_ e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia variáveis de ambiente e código da aplicação
COPY .env .
COPY app/ ./app
=

# 6. Comando padrão para iniciar o servidor
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
