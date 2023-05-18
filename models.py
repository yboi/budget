from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

# declarative base class
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[[str]] = mapped_column(String(30), unique=True)
    user_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))


        # with Session() as session:
        #     user = session.query().filter_by(login=login).first()
        #     if user:
        #         raise ValueError("Login already exists")
        #     session.add()
        #     session.commit()
        #     print(f"User {user_name} with email {email} created successfully! (login:{login}  password:{password})")
