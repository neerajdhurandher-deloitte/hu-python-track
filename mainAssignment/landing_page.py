from mainAssignment.pages.adminPage import Admin
from mainAssignment.pages.userPage import UserPage
from mainAssignment.customeExceptions.invalidInput import InputCheck


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
                user_db.print_movie_list()
            elif op == 3:
                exit()
            else:
                print("Invalid input !!  try again")


ob = landingPage()
ob.start()
