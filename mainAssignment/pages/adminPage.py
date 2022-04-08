# from mainAssignment.customeExceptions import InvalidCredential

from mainAssignment.utils import movie

from mainAssignment.utils.db import DB


class InvalidCredential(Exception):
    def __init__(self):
        super()

    def print_msg(self, message):
        print("Error ", message)


# movie_dict = {}


def str_val(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)


def time_formate(time):
    hours = int(time / 60)
    min = time - hours * 60
    if hours > 23:
        hours -= 24
    if min == 0:
        min = 00
    am_pm = " AM"
    if hours > 11:
        am_pm = " PM"
    if hours > 12:
        hours -= 12

    return "" + str_val(hours) + ":" + str_val(min) + am_pm


def get_show_timing(show_starting_time, total_length, gap_bt_show):
    show_start = time_formate(show_starting_time)
    show_end = time_formate(show_starting_time + total_length - gap_bt_show)

    return show_start + " to " + show_end


def cal_movie_show_timing(total_length, gap_bt_show, numShows, first_show):
    show_timing_list = []
    show_starting_time = first_show

    for show in range(numShows):
        show_time = get_show_timing(show_starting_time, total_length, gap_bt_show)
        show_timing_list.append(show_time)
        show_starting_time += total_length
    return show_timing_list


def show_count_validation(total_length, numShows, first_show):
    total_running_time = total_length * numShows
    available_time = 1440 - first_show * 60

    if total_running_time < available_time:
        return True
    elif total_running_time - available_time < total_length:
        return True
    else:
        # TODO remove this
        print("total_running_time ", total_running_time)
        print("available_time", available_time)
        return False


def show_timing_setup(length, interval_timing, gap_bt_show, numShows, first_show):
    total_length = length + interval_timing + gap_bt_show

    valid_show_setup = show_count_validation(total_length, numShows, first_show)

    while not valid_show_setup:
        print("Invalid shows setting !!")
        numShows = int(input("Enter movie's number of shows in a day :- "))
        valid_show_setup = show_count_validation(total_length, numShows, first_show)

    timings = cal_movie_show_timing(total_length, gap_bt_show, numShows, first_show * 60)

    return timings


def options_on_invalid_choice():
    print("1. Try again")
    print("2. Exit")
    op = int(input("choice :- "))
    return op


def edit_movie_info(editing_movie, param):
    new_input = input("Enter new " + param + " :- ")

    try:
        editing_movie.param = new_input
    except TypeError as e:
        editing_movie.param = int(new_input)
    finally:
        print("movie " + param + " info edit successfully")
        print("movie's edited info ", editing_movie)


class Admin(InvalidCredential, DB):
    # TODO create valid admin credential
    admin_dict = {"username": "a", "password": "1"}

    print("****** Welcome to Admin Login Page *******")

    def delete_movie(self):
        print("Delete a movie")

    def logout(self):
        print("Logout")

    def edit_movie(self):
        print("Edit movie's info")

        movie_name = input("Find movie for edit :- ")

        if DB.movie_dict.get(movie_name) is None:
            print("movie name doesn't exit")
            op = 0
            while op != 2:
                op = options_on_invalid_choice()
                if op == 1:
                    self.edit_movie()
                elif op == 2:
                    return
                else:
                    print("Invalid input")

        else:
            editing_movie = DB.movie_dict.get(movie_name)

            edit_choice = -1

            while edit_choice != 0:

                print("Which filed you want to edit")
                print("1. Title")
                print("2. genre")
                print("3. length")
                print("4. cast")
                print("5. director")
                print("6. admin rating")
                print("7. language")
                print("8. number of Shows")
                print("9. first_show")
                print("10. interval timing")
                print("11. gap between shows")
                print("12. seat capacity")
                print("0. Exit")

                edit_choice = int(input("Enter choice :- "))

                if edit_choice == 0:
                    self.go_to_admin_options()

                if edit_choice == 1:
                    op = 0
                    while op != 2:
                        new_tile = input("new title for movie:- ")

                        if DB.movie_dict.get(new_tile) is None:
                            editing_movie.title = new_tile
                            DB.movie_dict[new_tile] = DB.movie_dict[movie_name]
                            del DB.movie_dict[movie_name]

                        else:
                            print("Entered movie name already exits ")
                            op = options_on_invalid_choice()

                elif edit_choice == 2:
                    edit_movie_info(editing_movie, "genre")
                elif edit_choice == 3:
                    edit_movie_info(editing_movie, "length")
                elif edit_choice == 4:
                    edit_movie_info(editing_movie, "cast")
                elif edit_choice == 5:
                    edit_movie_info(editing_movie, "director")
                elif edit_choice == 6:
                    edit_movie_info(editing_movie, "admin_rating")
                elif edit_choice == 7:
                    edit_movie_info(editing_movie, "language")
                elif edit_choice == 8:
                    edit_movie_info(editing_movie, "numShow")
                elif edit_choice == 9:
                    edit_movie_info(editing_movie, "first_show")
                elif edit_choice == 10:
                    edit_movie_info(editing_movie, "interval_timing")
                elif edit_choice == 11:
                    edit_movie_info(editing_movie, "gap_bt_show")
                elif edit_choice == 12:
                    edit_movie_info(editing_movie, "seat_capacity")

    def add_new_movie(self):
        print("****** Add new movie info ******")
        title = input("Enter movie's title :- ")
        genre = input("Enter movie's Genre :- ")
        length = 60 * int(input("Enter movie's length (hours):- "))
        length += int(input("Enter movie's length (minutes):- "))
        cast = input("Enter movie's cast :- ")
        director = input("Enter movie's director :- ")
        admin_rating = float(input("Enter movie's admin rating (out of 10 ):- "))
        language = input("Enter movie's language :- ")

        numShows = int(input("Enter movie's number of shows in a day :- "))
        first_show = int(input("Enter timing of first shows of the day ( 24 hours formate ) :- "))
        interval_timing = int(input("Enter movie's interval timing  (int minutes) :- "))
        gap_bt_show = int(input("Enter the of gap timing between shows  (int minutes) :- "))
        seat_capacity = int(input("Enter seat capacity in theater :- "))

        timings = show_timing_setup(length, interval_timing, gap_bt_show, numShows, first_show)

        new_movie_obj = movie.Movie(self, title, genre, length, cast, director, admin_rating, 0.0, language, timings, numShows,
                                    first_show, interval_timing, gap_bt_show, seat_capacity)

        DB.movie_dict[title] = new_movie_obj

        DB.movie_list = new_movie_obj

        DB.show_movie_details(self, new_movie_obj)

        print(title, " Movie add successfully ")
        print("Available timings are ", timings)

        DB.show_movies_name(self)

    def go_to_admin_options(self):
        print("****** Welcome Admin *******")

        print("1. Add New Movie Info")
        print("2. Edit Movie Info ")
        print("3. Delete Movies ")
        print("4. Logout")
        sel_option = 0

        while sel_option != 4:
            sel_option = int(input("Enter your choice :- "))

            if sel_option == 1:
                self.add_new_movie()
            elif sel_option == 2:
                self.edit_movie()
            elif sel_option == 3:
                self.delete_movie()
            elif sel_option == 4:
                self.logout()

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
            self.go_to_admin_options()
        except InvalidCredential as e:
            e.print_msg("Invalid admin credentials")




