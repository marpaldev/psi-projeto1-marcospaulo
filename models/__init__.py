from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("sqlite:///biblioteca.db")

class Base(DeclarativeBase):
    pass

Base.metadata.create_all()