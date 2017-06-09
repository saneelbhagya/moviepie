import webbrowser
from video import Video


class Movie(Video):

    """Movie Class represents is a child Class of Video """
    # Constructor to create Movie instance.

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, genre):
        Video.__init__(self, title, storyline, genre)
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # method to open youtube trailer URL.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
