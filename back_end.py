from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# create a SQLite database
engine = create_engine('sqlite:///test_develop.db')

# create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# define a base model class
Base = declarative_base()

# define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name})>'

    @classmethod
    def create_user(cls, login, user_name, email, password):
        if cls.check_if_login_is_available(login):
            raise ValueError("Login already exists")
        user = cls(
            login=login,
            user_name=user_name,
            email=email,
            password=password
        )
        session.add(user)
        session.commit()
        session.close()
        print(f"User {user_name} with {email}, login {login} - created successfully!\n")
        cls.print_table()

    @classmethod
    def check_if_login_is_available(cls, login):
        user = session.query(cls).filter_by(login=login).first()
        if user:
            print("Login already exists")
            return True
        return False

    @classmethod
    def print_table(cls):
        users = session.query(cls).all()
        for user in users:
            print(f"ID: {user.id}, Name: {user.user_name}, Login: {user.login}, Email: {user.email}")

# create the table
Base.metadata.create_all(engine)

# user credentials
login = input("What login you wanna to use:\n")
user_name = input("Enter your name:\n")
email = input("Enter your email:\n")
password = input("Enter your password\n")

# create a new user
User.create_user(login=login, user_name=user_name, email=email, password=password)
