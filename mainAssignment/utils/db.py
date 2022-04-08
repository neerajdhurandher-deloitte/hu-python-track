from mainAssignment.utils import time_formate
class DB:
    user_list = []
    user_dic = {}
    movie_list = {}
    movie_dict = {}

    def print_movie_list(self):
        print(self.movie_dict)

    def print_users_list(self):
        print(self.user_dic)

    def show_movies_name(self):
        index = 1
        for movie_key, movie_value in self.movie_dict.items():
            try:
                print(str(index), " ", movie_key)
                index += 1
            except Exception as e:
                print(e)

    def show_movie_details(self, get_movie):
        length = get_movie.length

        print("Title : ", get_movie.title)
        print("Genre : ", get_movie.genre)
        print("Length : ", time_formate.min_to_hour_min(length))
        print("Cast : ", get_movie.cast)
        print("Director : ", get_movie.director)
        print("Admin rating : ", get_movie.admin_rating)
        print("Timings are : ", get_movie.timings)
        print("User rating : ", get_movie.user_rating)
