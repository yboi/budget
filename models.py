from sqlalchemy.orm import declarative_base
from create_db import engine

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
Session = sessionmaker(bind=engine)


class CreateUser(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[[str]] = mapped_column(String(30), unique=True)
    user_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))

    def __init__(self, login, user_name, email, password):
        self.login = login
        self.user_name = user_name
        self.email = email
        self.password = password

        with Session() as session:
            user = session.query(CreateUser).filter_by(login=self.login).first()
            if user:
                raise ValueError("Login already exists")
            session.add(self)
            session.commit()
            print(f"User {self.user_name} with email {self.email} created successfully! (login:{self.login}  password:{self.password})")
