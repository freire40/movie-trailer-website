import webbrowser

class Movie():
    """This Class stores movie related information:
    Title
    Storyline
    Year
    IMDB rating
    PG UK
    PG US
    Cast
    Director
    Genre
    Poster image
    trailer video"""

    VALID_RATINGS_US = ["G", "PG", "PG-13", "R", "NC-17"]
    VALID_RATINGS_UK = ["U", "PG", "12A", "12", "15", "18", "R18"]

    def __init__(self,
                movie_title,
                movie_storyline,
                movie_year,
                movie_imdb_rating,
                movie_pg_uk,
                movie_pg_us,
                movie_cast,
                movie_director,
                movie_genre,
                poster_image,
                trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = movie_year
        self.imdb_rating = movie_imdb_rating
        self.pg_uk = movie_pg_uk
        self.pg_us = movie_pg_us
        self.cast = movie_cast
        self.director = movie_director
        self.genre = movie_genre
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
