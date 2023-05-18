from models import User
from config import db_name
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(f"sqlite:///{db_name}")

with Session(engine) as session:
    new_user = User(
        login="Bob",
        user_name="bob_1",
        email="bob@email.com",
        password="password_1")
    session.add(new_user)
    session.commit()

