# from mainAssignment.customeExceptions import InvalidCredential
class InvalidCredential(Exception):
    def __init__(self):
        super()

    def print_msg(self, message):
        print("Error ", message)


movie_dict = {}


def cal_movie_show_timing(total_length, numShows, first_show):
    pass


def show_count_validation(total_length, numShows, first_show):
    total_running_time = total_length * numShows
    available_time = 1440 - first_show * 60

    print("total_running_time ", total_running_time)
    print("available_time", available_time)

    if total_running_time < available_time:
        print("true")
        return True
    elif total_running_time - available_time < total_length:
        print(" next day true", total_running_time - available_time)
        return True
    else:
        print("false")
        return False


def add_new_movie():
    print("****** Add new movie info ******")
    # title = input("Enter movie's title :- ")
    # genre = input("Enter movie's Genre :- ")
    length = 60 * int(input("Enter movie's length (hours):- "))
    length += int(input("Enter movie's length (minutes):- "))
    # cast = input("Enter movie's cast :- ")
    # director = input("Enter movie's director :- ")
    # admin_rating = int(input("Enter movie's admin rating :- "))
    # language = input("Enter movie's language :- ")

    numShows = int(input("Enter movie's number of shows in a day :- "))
    first_show = int(input("Enter timing of first shows of the day ( 24 hours formate ) :- "))
    interval_timing = int(input("Enter movie's interval timing  (int minutes) :- "))
    gap_bt_show = int(input("Enter the of gap timing between shows  (int minutes) :- "))
    # seat_capacity = int(input("Enter seat capacity in theater :- "))

    total_length = length + interval_timing + gap_bt_show

    valid_show_setup = show_count_validation(total_length, numShows, first_show)

    while not valid_show_setup:
        print("Invalid shows setting !!")
        numShows = int(input("Enter movie's number of shows in a day :- "))
        valid_show_setup = show_count_validation(total_length, numShows, first_show)
    print("valid")

    # timings = cal_movie_show_timing(total_length, numShows, first_show)


def edit_movie():
    print("Edit movie's info")


def delete_movie():
    print("Delete a movie")


def logout():
    print("Logout")


def go_to_admin_options():
    print("****** Welcome Admin *******")

    print("1. Add New Movie Info")
    print("2. Edit Movie Info ")
    print("3. Delete Movies ")
    print("4. Logout")
    sel_option = 0

    while sel_option != 4:
        sel_option = int(input("Enter your choice :- "))

        if sel_option == 1:
            add_new_movie()
        elif sel_option == 2:
            edit_movie()
        elif sel_option == 3:
            delete_movie()
        elif sel_option == 4:
            logout()


class Admin(InvalidCredential):
    # TODO create valid admin credential
    admin_dict = {"username": "a", "password": "1"}
    print("****** Welcome to Admin Login Page *******")

    def log_in_credential(self):
        username = input("Enter admin username :- ")
        password = input("Enter password :- ")

        try:
            get_username = self.admin_dict.get('username')
            get_password = self.admin_dict.get('password')

            if get_username != username:
                raise InvalidCredential
            while get_password != password:
                print("Incorrect password")
                password = input("Enter password :- ")
            go_to_admin_options()
        except InvalidCredential as e:
            e.print_msg("Invalid admin credentials")


# ob = Admin()
# ob.log_in_credential()
add_new_movie()
