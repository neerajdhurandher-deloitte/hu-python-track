from mainAssignment.customeExceptions.invalidCredential import InvalidCredential
from mainAssignment.utils import movie, user
from mainAssignment.pages import homePage
from mainAssignment.utils.db import DB

user_list = []
user_dic = {}


def register_user():
    print("****Create new Account***** ")
    username = input("Enter your username :- ")
    name = input("Enter your name :- ")
    email = input("Enter your email :- ")
    phone = input("Enter your phone number :- ")
    age = input("Enter your age :- ")
    password = input("Enter your password :- ")

    new_user = user.User(username, name, email, phone, age, password)

    if user_dic.get(username) is None:
        user_dic[username] = new_user
        user_list.append(user_dic)
        print("User created")
        print(user_list)
    else:
        print("user already exits")


def user_login():
    print("****** Welcome to Book MyShow ******* ")
    print("********** User Login **********")

    username = input("Enter username :- ")
    password = input("Enter password :- ")

    if user_dic.get(username) is None:
        print("User not exits")
    else:
        user_temp = user_dic.get(username)

        if user_temp.username == username and user_temp.password == password :
            home_page = homePage.HomePage()
            home_page.welcome(user_temp)


def welcome_page():
    print("Welcome")
    print("1. Login")
    print("2. Register new account")
    print("3. Exit")

    choice = int(input("Enter :- "))
    return choice


class UserPage(InvalidCredential, DB):

    def __init__(self):
        pass

    def user_page(self):
        choice = welcome_page()

        while choice != 3:
            if choice == 1:
                user_login()

            elif choice == 2:
                register_user()
            else:
                print("Invalid choice , try again")
            choice = welcome_page()


