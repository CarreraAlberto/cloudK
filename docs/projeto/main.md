# Explicação do Projeto
A CloudK API é uma aplicação RESTful desenvolvida em Python com FastAPI, que permite:

Registrar usuários com email e senha (armazenando apenas o hash da senha com bcrypt);

Autenticar usuários e gerar tokens JWT com validade configurável;

Consultar dados protegidos (JSON estático do índice Bovespa dos últimos 10 dias) mediante token válido.

# Como Executar a Aplicação

Clone o repositório
```sh
git clone https://github.com/CarreraAlberto/cloudK.git"

```

Ajuste as variáveis no arquivo api/.env

variáveis sensíveis (credentials, secret JWT)

```sh
# Credenciais do Postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
DATABASE_HOST=database
DATABASE_PORT=5432

# Configurações do JWT
JWT_SECRET=@cloudk
JWT_ALGO=HS256
JWT_EXPIRY_MIN=60
```
Execute com Docker Compose:

```sh
docker compose up -d
```

# Documentação dos Endpoints
| Endpoint      | Método | Descrição                                       | Requisição                                      |
|---------------|--------|-------------------------------------------------|-------------------------------------------------|
| `/registrar`  | POST   | Cria novo usuário e retorna o token JWT         | JSON `{ "email": "...", "senha": "..." }`       |
| `/login`      | POST   | Valida credenciais e retorna o token JWT        | JSON `{ "email": "...", "senha": "..." }`       |
| `/consultar`  | GET    | Retorna JSON protegido (Bovespa últimos 10 dias)| Header `Authorization: Bearer <JWT>`            |


# Capturas de tela dos endpoints testados