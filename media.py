# A template to create multiple movie objects
class Movies():
    def __init__(
                 self,
                 movie_title,
                 movie_storyline,
                 trailer_youtube,
                 movie_poster
                 ):
        self.title = movie_title  # The title of the movie object
        self.storyline = movie_storyline  # The storyline of the movie object
        self.trailer_youtube_url = trailer_youtube  # The trailer url of movie
        self.poster_image = movie_poster  # The poster image of movie object
