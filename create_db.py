import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db_name = "main.db"
engine = create_engine(f"sqlite:///{db_name}")

if os.path.isfile(db_name):
    print("DB is exists")
else:
    Base.metadata.create_all(engine)
    print("DB is not found")
