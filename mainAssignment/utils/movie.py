class Movie:
    def __init__(self, movie_id, title, genre, length, cast, director, admin_rating, user_rating, language, timings, numShows, first_show,
                 interval_timing, gap_bt_show, seat_capacity, available_seat):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.length = length
        self.cast = cast
        self.director = director
        self.admin_rating = admin_rating
        self.user_rating = user_rating
        self.language = language
        self.timings = timings
        self.numShows = numShows
        self.first_show = first_show
        self.interval_timing = interval_timing
        self.gap_bt_show = gap_bt_show
        self.seat_capacity = seat_capacity
        self.available_seat = available_seat
