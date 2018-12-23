import webbrowser


class Movie ():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ This function it's responsable for the movie attributes
            Attributes:
            movie_title (str)
            movie_storyline (str)
            poster_image (str)
            trailer_youtube (str)"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
