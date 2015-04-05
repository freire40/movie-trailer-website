import os
import re

# Styles and scripting for the page
main_page_head = '''
<!doctype html>
<html>

<head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <title>Movie Trailer Website - a preview</title>
   <link rel="stylesheet" href="css/main.css">
   <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
   <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

   <script type="text/javascript"  >
      // Pause the video when the modal is closed
      $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
         // Remove the src so the player itself gets removed, as this is the only
         // reliable way to ensure the video stops playing in IE
         $("#trailer-video-container").empty();
      });
      // Start playing the video whenever the trailer modal is opened
      $(document).on('click', '.movie-row', function (event) {
         var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
         var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
         $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'frameborder': 0
         }));
      });
   </script>
</head>
'''

# The main page layout and title bar
main_page_body = '''
<body>
   <!-- Trailer Video Modal -->
   <div class="modal" id="trailer">
     <div class="modal-dialog">
      <div class="modal-content">
         <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
           <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="X">
         </a>
         <div class="scale-media" id="trailer-video-container">
         </div>
      </div>
     </div>
   </div>

   <div class="container">

      <!-- header -->
      <div class="row">
         <div class="col-md-12 top-banner">
            <!-- banner image: /images/theatre_room.png -->
            <!-- temporarily being loaded from css top-banner class -->
            <!-- TODO: find a way to make it resizable (and responsive) -->
            <!-- TODO: nav bar, fixed, top, with the behaviour of udacity initial page... -->
            <!--       that becomes visible when page scrolls up -->
            <div class="row">
               <div class="col-md-8 text-right text-uppercase">
                  <h1 class="title-size text-negative">movie trailer<span class="text-thick"> website</span></h1>
               </div>
               <div class="col-md-4"></div>
            </div>
            <div class="row">
               <div class="col-md-8"></div>
               <div class="col-md-4">
                  <h3 class="text-negative">... a preview</h3>
               </div>
            </div>
         </div>
      </div>

      <!-- section separator -->
      <div class="row">
         <div class="col-md-12">
            <h2>Web Movies</h2>
         </div>
      </div>
      <div class="row">
         <div class="col-md-12">
            <hr class="banner-separator">
         </div>
      </div>
      {movie_tiles}
      <!-- footer -->
      <div class="row">
         <div class="col-md-12">
            <hr>
            <p>FF 2015</p>
         </div>
      </div>
   </div>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
      <!-- movie row -->
      <div class="row movie-row" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
         <div class="col-md-3">
            <img width="220" height="342"  src="{poster_image_url}" alt="movie poster"/>
         </div>
         <div class="col-md-9">
            <!-- movie title and rating -->
            <div class="row">
               <div class="col-md-9">
                  <h4 class="movie-title-size">{movie_title} ({movie_year})</h4>
                  <p class="text-separator">{movie_pg_us} | {movie_genre}</p>
               </div>
               <div class="col-md-3 text-right">
                  <h4 class="movie-title-size">{movie_imdb_rating}</h4>
                  <p>IMDb</p>
               </div>
            </div>
            <!-- movie storyline, director and cast -->
            <div class="row">
               <div class="col-md-12">
                  <p>{movie_storyline}</p>
               </div>
               <div class="col-md-12">
                  <p><b>Director:</b> {movie_director}</p>
                  <p><b>Cast:</b> {movie_cast}</p>
               </div>
            </div>
         </div>
      </div>
'''

movie_tile_separator = '''
      <!-- movie separator -->
      <div class="row">
         <div class="col-md-3"></div>
         <div class="col-md-9">
            <hr class="film-separator">
         </div>
      </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile separator
        if content != '':
            content += movie_tile_separator

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            movie_storyline = movie.storyline,
            movie_year = movie.year,
            movie_imdb_rating = movie.imdb_rating,
            movie_pg_uk = movie.pg_uk,
            movie_pg_us = movie.pg_us,
            movie_cast = movie.cast,
            movie_director = movie.director,
            movie_genre = movie.genre,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def render_movies_page(movies, output_file_name):
    output_file = open(output_file_name, 'w')
    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_body.format(movie_tiles=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
