from mainAssignment.utils import time_formate
from mainAssignment.utils import movie


class DB:
    user_list = []
    user_dic = {}
    movie_list = []
    movie_dict = {}

    def print_movie_list(self):
        print(self.movie_dict)

    def print_users_list(self):
        print(self.user_dic)

    def show_movies_name(self):
        index = 1
        # for movie_key, movie_value in self.movie_dict.items():
        #     try:
        #         print(str(index), " ", movie_key)
        #         index += 1
        #     except Exception as e:
        #         print(e)
        for item in self.movie_list:
            try:
                print(str(index), " ", item.title)
                index += 1
            except Exception as e:
                print(e)

    def show_movie_details(self, get_movie_index):
        param = self.movie_list[get_movie_index]
        length = param.length

        print("Title : ", param.title)
        print("Genre : ", param.genre)
        print("Length : ", time_formate.min_to_hour_min(length))
        print("Cast : ", param.cast)
        print("Director : ", param.director)
        print("Admin rating : ", param.admin_rating)
        print("Timings are : ", param.timings)
        print("User rating : ", param.user_rating)
