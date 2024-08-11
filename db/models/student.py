from sqlalchemy.orm import Mapped , mapped_column
from . import Config

class Student(Config.BASE):
    __tablename__ = "students"

    name: Mapped[str]