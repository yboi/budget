from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///production.db")


Base = declarative_base()


def register_user(username, password, email):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # create a new user
    new_user = User(username=username, password=password, email=email)

    # add the user to the session and commit the transaction
    session.add(new_user)
    session.commit()

    print('User created successfully!')


class User(Base):
    def __int__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)


Base.metadata.create_all(engine)
