from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create a SQLite database
engine = create_engine('sqlite:///test_develop.db')

# create a session factory
Session = sessionmaker(bind=engine)
session = Session()
# define a base model class
Base = declarative_base()

# user credentials
login = input("What login you wanna to use:\n")
user_name = input("Enter your name:\n")
email = input("Enter your email:\n")
password = input("Enter you password\n")

# define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name})>'

# create the table
Base.metadata.create_all(engine)


# define a method to insert a new user
def create_user(login, user_name, email, password):
    if check_if_login_is_available(login):
        raise ValueError("Login already exists")
    session = Session()
    user = User(
        login=login,
        user_name=user_name,
        email=email,
        password=password
    )
    session.add(user)
    session.commit()
    session.close()
    print(f'User {user_name}  with {email}, login {login} - created successfully!')
    print_table()


def check_if_login_is_available(login):
    users = session.query(User).all()
    for user in users:
        if user.login == login:
            message = "Login already exists"
            print(message)
            return True


def print_table():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.user_name}, Login: {user.login}, Email: {user.email}")


# insert a new user
create_user(login, user_name, email, password)
