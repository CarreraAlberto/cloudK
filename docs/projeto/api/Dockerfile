# imagem Docker da aplicação

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY app/ ./app

EXPOSE 8080

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
