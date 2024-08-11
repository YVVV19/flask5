from sqlalchemy.orm import Mapped , mapped_column
from . import Config

class Group(Config.BASE):
    __tablename__ = "groupd"

    name: Mapped[str]