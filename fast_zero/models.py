from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# Mapped refere-se a um atributo Python que é associado
# (ou mapeado)
# a uma coluna específica em uma tabela de banco de dados.
# Por exemplo,
# Mapped[int] indica que este atributo é um inteiro que será
# mapeado para uma coluna correspondente em uma tabela de banco de dados.

table_registry = registry()


# registry() Usado para registrar e mapear classes Python
# como tabelas no banco de dados.
# Substitui o uso mais antigo de Base = declarative_base()
# com uma abordagem mais explícita


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


# init não tem uma relação direta com o banco de dados,
# mas sim com a forma em que vamos usar o objeto do modelo no
# código.
# Ele diz que os atributos marcados com init=false
# não devem ser passados no momento em que User for instanciado.
