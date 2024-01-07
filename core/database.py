from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'sqlite:///store.db'

engine = create_engine(DATABASE_URL, echo=True)
session_maker = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
