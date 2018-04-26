# A template to create movie movie objects
class Movies():
    def __init__(
                 self, movie_title,
                 movie_storyline,
                 trailer_youtube,
                 movie_poster
                 ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image = movie_poster
