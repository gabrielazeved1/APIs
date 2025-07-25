from dataclasses import asdict
from sqlalchemy import select
from fast_zero.models import User


def test_create_user(session):
    new_user = User(username="alice", password="secret", email="teste@test")
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "alice"))
    #tudo que vier do banco transformado em objeto Python
    assert user.username == "alice"

    assert asdict(user) == { 
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,  
    }