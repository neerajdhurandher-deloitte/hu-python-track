from mainAssignment.pages.adminPage import Admin
from mainAssignment.pages.userPage import UserPage


class landingPage():
    def start(self):
        # admin_ob.log_in_credential()
        admin_ob = Admin()
        # admin_ob.print_movie_list()
        admin_ob.add_new_movie()
        admin_ob.print_movie_list()
        # admin_ob.edit_movie()

        user_db = UserPage()
        print("User login")
        user_db.print_movie_list()

ob = landingPage()
ob.start()