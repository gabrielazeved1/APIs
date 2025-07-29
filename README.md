# Projeto fast_zero: API RESTful com FastAPI

Este repositório apresenta o desenvolvimento de uma API RESTful utilizando o framework web **FastAPI**, focado na criação eficiente de serviços web com tipagem de dados e validação automática. O projeto visa demonstrar proficiência em desenvolvimento de APIs Python, gerenciamento de dependências, testes e práticas de qualidade de código.

## Tecnologias Utilizadas

* **FastAPI**: Framework web moderno e de alta performance para a construção de APIs com Python 3.7+.
* **SQLAlchemy**: Toolkit SQL e Object Relational Mapper (ORM) para interação com o banco de dados.
* **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy, permitindo evoluir o schema do banco de dados de forma controlada.
* **Poetry**: Ferramenta para gerenciamento de dependências e ambientes virtuais Python, garantindo consistência e reprodutibilidade do projeto.
* **Pydantic**: Biblioteca para validação e parse de dados usando type hints Python. Essencial para a tipagem dos schemas de requisição e resposta.
* **Ruff**: Linter e formatador de código Python extremamente rápido, garantindo a padronização e qualidade do código.
* **Pytest**: Framework de teste completo e flexível para escrever e executar testes unitários e de integração.
* **Passlib (pwdlib)**: Biblioteca para hashing e verificação de senhas de forma segura.
* **PyJWT**: Implementação de JSON Web Tokens (JWT) para autenticação segura na API.
* **Uvicorn**: Servidor ASGI de alta performance para executar aplicações FastAPI.
* **SQLite**: Banco de dados leve e embarcado, utilizado para o desenvolvimento local.

## Funcionalidades da API

A API `fast_zero` oferece os seguintes endpoints para gerenciamento de usuários e autenticação:

* **`GET /`**:
    * **Descrição**: Endpoint inicial que retorna uma mensagem de boas-vindas.
    * **Resposta**: `{"message": "Olá Mundo!"}`

* **`POST /users/`**:
    * **Descrição**: Cria um novo usuário no sistema.
    * **Corpo da Requisição**:
        ```json
        {
          "username": "novo_usuario",
          "email": "email@example.com",
          "password": "senha_segura"
        }
        ```
    * **Validações**:
        * Verifica se o `username` ou `email` já estão em uso, retornando um erro `HTTP 409 Conflict`.
    * **Resposta de Sucesso (HTTP 201 Created)**:
        ```json
        {
          "id": 1,
          "username": "novo_usuario",
          "email": "email@example.com"
        }
        ```

* **`GET /users/`**:
    * **Descrição**: Retorna uma lista paginada de usuários.
    * **Parâmetros de Consulta**:
        * `skip`: Número de registros a serem pulados (para paginação).
        * `limit`: Número máximo de registros a serem retornados.
    * **Resposta**:
        ```json
        [
          {
            "id": 1,
            "username": "usuario1",
            "email": "usuario1@example.com"
          },
          {
            "id": 2,
            "username": "usuario2",
            "email": "usuario2@example.com"
          }
        ]
        ```

* **`PUT /users/{user_id}`**:
    * **Descrição**: Atualiza os dados de um usuário existente.
    * **Requer**: Autenticação via `Bearer Token` (JWT). O usuário autenticado deve ter permissão para modificar o `user_id` especificado (i.e., ser o próprio usuário ou ter permissão de administrador, se implementado).
    * **Parâmetros de Path**:
        * `user_id`: ID do usuário a ser atualizado.
    * **Corpo da Requisição**:
        ```json
        {
          "username": "novo_nome_usuario",
          "email": "novo_email@example.com",
          "password": "nova_senha_segura"
        }
        ```
    * **Validações**:
        * Verifica se o novo `username` ou `email` já estão em uso por outro usuário.
        * Retorna `HTTP 404 Not Found` se o usuário não for encontrado.
        * Retorna `HTTP 401 Unauthorized` se o token for inválido ou ausente.
        * Retorna `HTTP 403 Forbidden` se o usuário autenticado não tiver permissão.
    * **Resposta de Sucesso (HTTP 200 OK)**:
        ```json
        {
          "id": 1,
          "username": "novo_nome_usuario",
          "email": "novo_email@example.com"
        }
        ```

* **`DELETE /users/{user_id}`**:
    * **Descrição**: Exclui um usuário do sistema.
    * **Requer**: Autenticação via `Bearer Token` (JWT). O usuário autenticado deve ter permissão para excluir o `user_id` especificado.
    * **Parâmetros de Path**:
        * `user_id`: ID do usuário a ser excluído.
    * **Validações**:
        * Retorna `HTTP 404 Not Found` se o usuário não for encontrado.
        * Retorna `HTTP 401 Unauthorized` se o token for inválido ou ausente.
        * Retorna `HTTP 403 Forbidden` se o usuário autenticado não tiver permissão.
    * **Resposta de Sucesso (HTTP 204 No Content)**: Não retorna conteúdo.

* **`POST /token`**:
    * **Descrição**: Endpoint para autenticação de usuários, retornando um JWT (JSON Web Token) para acesso aos endpoints protegidos.
    * **Corpo da Requisição (Form Data - `application/x-www-form-urlencoded`)**:
        ```
        username=seu_email@example.com&password=sua_senha
        ```
    * **Resposta de Sucesso (HTTP 200 OK)**:
        ```json
        {
          "access_token": "seu_token_jwt_aqui",
          "token_type": "bearer"
        }
        ```
    * **Resposta de Erro (HTTP 401 Unauthorized)**: Credenciais inválidas.

## Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

* Python 3.11 (ou superior)
* Poetry

### 1. Clonar o Repositório (Exemplo, se fosse um repositório Git real)

```bash
git clone git@github.com:gabrielazeved1/APIs.git
cd fast_zero
```
## 2. Configuração do Ambiente

Ajuste a versão do Python para garantir a compatibilidade do Poetry:

```bash
poetry env use python3.11
```

Instale as dependências do projeto:

```bash
poetry install
```

---

## 3. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto, baseado no `example.env`, e configure a URL do banco de dados e a chave secreta para JWT:

```ini
# .env
DATABASE_URL="sqlite:///database.db"
SECRET_KEY="sua_chave_secreta_segura_aqui"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 4. Migrações do Banco de Dados

Aplique as migrações do banco de dados para criar as tabelas necessárias:

```bash
poetry run alembic upgrade head
```

---

## 5. Executar a Aplicação

Inicie o servidor Uvicorn:

```bash
poetry run task run
# ou diretamente:
poetry run uvicorn fast_zero.app:app --reload
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Documentação Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Documentação ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Para parar o servidor, pressione `Ctrl + C`.

---

## Mantendo a Qualidade do Código

Utilizamos o **Ruff** para linting e formatação de código.

### Verificar Problemas

```bash
poetry run task lint
# ou:
poetry run ruff check .
```

### Corrigir Problemas Automaticamente (Pré-formatação)

```bash
poetry run task pre_format
# ou:
poetry run ruff check . --fix
```

### Formatar Código Completamente

```bash
poetry run task format
# ou:
poetry run ruff format .
```

---

## Testes

O projeto inclui testes para garantir a corretude das funcionalidades da API.

### Executar Testes

```bash
poetry run task test
# ou:
poetry run pytest --cov=fast_zero --cov-report=term-missing tests/
```

### Detalhes dos Arquivos de Teste

- `tests/test_app.py`: Testes de integração dos endpoints
- `tests/test_db.py`: Testes de operações básicas no banco
- `tests/test_security.py`: Testes de hash de senha e JWT
- `tests/conftest.py`: Fixtures para testes com banco SQLite em memória

---

## Gerenciamento de Dependências com Poetry

### Adicionar uma dependência de produção:

```bash
poetry add nome-da-biblioteca
# Exemplo:
poetry add requests
```

### Adicionar uma dependência de desenvolvimento:

```bash
poetry add --group dev nome-da-biblioteca
# Exemplo:
poetry add --group dev ipython
```

### Remover uma dependência:

```bash
poetry remove nome-da-biblioteca
```

### Instalar dependências de um projeto clonado:

```bash
poetry install
```

### Instalar apenas dependências de produção:

```bash
poetry install --no-root --without dev
```

---

## Análise de Segurança de Senhas 

Para verificar as senhas armazenadas no banco de dados (somente em ambiente de desenvolvimento):

### Acessar o shell do Poetry:

```bash
poetry shell
```

### Iniciar o cliente SQLite:

```bash
sqlite3 database.db
```

### Comandos no SQLite:

```sql
.tables
SELECT * FROM users;
.quit
```

### Sair do shell Poetry:

```bash
exit
```
