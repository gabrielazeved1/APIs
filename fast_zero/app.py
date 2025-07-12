from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    """
    Cria uma instância do modelo UserDB a partir dos dados recebidos
    no corpo da requisição.

    - `user`: é uma instância de UserSchema (modelo de entrada)
      validada automaticamente pelo FastAPI.
    - `user.model_dump()`: converte o objeto Pydantic em um dicionário
      com os campos informados pelo cliente.
    - `**user.model_dump()`: desempacota esse dicionário para passar
      os campos como argumentos nomeados.
    - `id=len(database) + 1`: gera um ID sequencial com base na
      quantidade atual de usuários armazenados localmente.

    O resultado é um objeto UserDB com todos os dados do usuário
    mais o campo `id`, pronto para ser armazenado e retornado.
    """
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", response_model=UserList)
def read_user():
    return {"users": database}


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, DETAIL="User not found"
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    del database[user_id - 1]

    return {"message": "User deleted"}
