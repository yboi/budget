import os.path
from models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_name = "main.db"
engine = create_engine(f"sqlite:///{db_name}")
Session = sessionmaker(bind=engine)
session = Session()

if os.path.isfile(db_name):
    # engine.connect()
    print("DB is exists")
else:
    Base.metadata.create_all(engine)
    print("DB is not found")
