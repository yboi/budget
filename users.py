from create_db import *

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[[str]] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))


    # https://docs.sqlalchemy.org/en/20/core/dml.html

    def create_user(login, user_name, email, password):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.filter_by
        user = session.query(User).filter_by(login=login).first()
        if user:
            raise ValueError("Login already exists")
        user = User(login=login, user_name=user_name, email=email, password=password)
        session.add(user)
        session.commit()
        session.close()
        print(f'User {user_name} with email {email} created successfully!')


Base.metadata.create_all(engine)
User.create_user(
    login=input("What login name you wanna to use:\n"),
    user_name=input("Enter your name:\n"),
    email=input("Enter your email:\n"),
    password=input("Enter you password\n")
)



