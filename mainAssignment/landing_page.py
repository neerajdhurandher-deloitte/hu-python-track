from mainAssignment.pages.adminPage import Admin
from mainAssignment.pages.userPage import UserPage
from mainAssignment.customeExceptions.invalidInput import InputCheck
from mainAssignment.utils.db import DB
from mainAssignment.utils.movie import Movie
from mainAssignment.utils.user import User


class landingPage(InputCheck):
    def start(self):
        op = 0

        while op != 3:
            print("******Welcome to BookMyShow******* ")
            print("1. Admin")
            print("2. User")
            print("3. Exit")

            op = InputCheck.int_input_check("Enter your choice :- ")
            if op == 1:
                admin_ob = Admin()
                admin_ob.log_in_credential()

            elif op == 2:
                user_db = UserPage()
                print("User login")
                user_db.user_page()
            elif op == 3:
                exit()
            else:
                print("Invalid input !!  try again")


# Demo movie
new_movie = Movie("1", "Demo Movie", "Demo Genre", 190, "Demo  Cast", "Demo director", 3.0, 0.0, "Demo language",
                  ["1pm to 2pm", "3pm to 4pm"], 2, 8, 5, 5,
                  10, 10)
DB.movie_dict["1"] = new_movie
DB.movie_list.append(new_movie)

# Demo User
new_user = User("demo", "Demo User", "demo@gmail.com", "1234567890", 21, "123")
DB.user_dic["demo"] = new_user
DB.user_list.append(new_user)

ob = landingPage()
ob.start()
