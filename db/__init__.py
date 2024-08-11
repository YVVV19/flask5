from .config import Config
from sqlalchemy import select
from .models import Users, Student, Group

# def migrate():
#     with Config.SESSION() as session:
#         for i in range(10):
#             session.add(student(name=f"Vasya{i+1}"))
#         session.commit()


def user_create(nickname:str):
    with Config.SESSION() as session:
        session.add(Users(nickname=nickname))
        session.commit()


def user_select(nickname:str):
    with Config.SESSION() as session:
        query = select(Users.nickname==nickname)
        result = session.scalars(query).first()
        print(result)