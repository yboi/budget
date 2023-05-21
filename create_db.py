import os.path
from config import db_name
from sqlalchemy import create_engine
from models import Base

engine = create_engine(f"sqlite:///{db_name}")

if os.path.isfile(db_name):
    print("DB is exists")
else:
    Base.metadata.create_all(engine)
    print("DB is not found")

Base.metadata.create_all(engine)
