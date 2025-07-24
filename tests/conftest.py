import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from contextlib import contextmanager
from datetime import datetime

from fast_zero.app import app
from fast_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # Cria um banco SQLite na memória RAM, que é descartado ao fim do teste.
    engine = create_engine("sqlite:///:memory:")
    # Cria todas as tabelas definidas no registry.
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
    # Após o teste, remove todas as tabelas criadas. 


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook)
    yield time
    event.remove(model, 'before_insert', fake_time_hook)



@pytest.fixture
def mock_db_time():
    return _mock_db_time
    #hooks =  antes de inserir faca algo