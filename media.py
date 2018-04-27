# A template to create multiple movie objects
class Movies():
    def __init__(
                 self,
                 movie_title,
                 movie_storyline,
                 trailer_youtube,
                 movie_poster
                 ):
        self.title = movie_title
        # Represent the title of the movie object
        self.storyline = movie_storyline
        # Represent the storyline of the movie object
        self.trailer_youtube_url = trailer_youtube
        # Represent the youtube url of the movie object
        self.poster_image = movie_poster
        # Represent the poster image of the movie object
