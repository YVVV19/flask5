from sqlalchemy.orm import Mapped
from . import Config

class Users(Config.BASE):
    __tablename__ = "users"
    
    nickname:Mapped[str]