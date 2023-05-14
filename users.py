from models import CreateUser

CreateUser(
    login=input("What login name you wanna to use:\n"),
    user_name=input("Enter your name:\n"),
    email=input("Enter your email:\n"),
    password=input("Enter you password\n")
)
