import webbrowser
from video import Video

class Movie(Video):
    """docstring for ."""
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, genre):
        Video.__init__(self,title,storyline,genre)
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
