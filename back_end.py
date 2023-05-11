from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask import Flask, render_template, request


# create a SQLite database
engine = create_engine('sqlite:///test_develop.db')
# create a session factory
Session = sessionmaker(bind=engine)
session = Session()
# define a base model class
Base = declarative_base()
# user credentials
login = input("What login name you wanna to use:\n")
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


def create_user(user_name, login, email, password):
    if check_if_login_is_available(login=login):
        raise ValueError("Login already exists")
    session = Session()
    user = User(
        user_name=user_name,
        login=login,
        email=email,
        password=password
    )
    session.add(user)
    session.commit()
    session.close()
    print(f'User {user_name}  with {email} created successfully!')
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
        print(f"ID: {user.id}, Name: {user.user_name}, Email: {user.email}")


# insert a new user
create_user(login, user_name, email, password)

app = Flask(__name__)


@app.route('/register')
def register():
    error = request.args.get('error')
    return render_template('register.html', error=error)


@app.route('/register', methods=['POST'])
def register():
    login = request.form['login']
    user_name = request.form['user_name']
    email = request.form['email']
    password = request.form['password']
    # create a new user object and add it to the database
    user = User(login=login, user_name=user_name, email=email, password=password)
    session.add(user)
    session.commit()
    return 'Registration successful!'
