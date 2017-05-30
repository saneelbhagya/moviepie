import webbrowser

class Movie(object):
    """docstring for ."""
    def __init__(self, title, storyline, poster_image, youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.youtube_trailer = youtube_trailer


    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
