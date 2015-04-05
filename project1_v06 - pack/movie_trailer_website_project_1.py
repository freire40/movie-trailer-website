import tomatoes_squeezer
import media
import os
import webbrowser


OUTPUT_FILE_NAME = 'movie_trailer_website.html'
MOVIE_NUM_FIELDS = 11

#Movia data information is imported from this file:
MOVIES_DATA_FILE = "movie_info.txt"


def import_movies():
    # file structure: 1 field per line, blank line as a movie separator
    # movie field sequence must be as defined in class Media:
        ##    0.Title
        ##    1.Storyline
        ##    2.Year
        ##    3.IMDB rating
        ##    4.PG UK
        ##    5.PG US
        ##    6.Cast
        ##    7.Director
        ##    8.Genre
        ##    9.Poster_link
        ##    10. Trailer_link

    # TODO: get a more structured way of loading from excel table
    # TODO: get movie data such as ratings from imdb-like sites
    
    file = open(MOVIES_DATA_FILE, 'r')
    movies = []
    end_of_file = 0
    while end_of_file != '':
        movie_fields = [file.readline().rstrip('\n ') for i in range(MOVIE_NUM_FIELDS)]
        movies.append(media.Movie(movie_fields[0],
                                  movie_fields[1],
                                  movie_fields[2],
                                  movie_fields[3],
                                  movie_fields[4],
                                  movie_fields[5],
                                  movie_fields[6],
                                  movie_fields[7],
                                  movie_fields[8],
                                  movie_fields[9],
                                  movie_fields[10]))
        # skip blank line separator, at same time check for EOF
        end_of_file = file.readline()
    #for a in movies:
    #    print("filme: " + a.title)
    return movies


# real action starts here:
movies = import_movies()
tomatoes_squeezer.render_movies_page(movies, OUTPUT_FILE_NAME)

# open the output file in the browser
url = os.path.abspath(OUTPUT_FILE_NAME)
webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
