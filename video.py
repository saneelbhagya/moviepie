"""Video Class represents a video entity like a movie,
   tv show or any short film """


class Video(object):
    # Constructs an instance of Video class
    def __init__(self, title, storyline, genre):
        self.title = title
        self.storyline = storyline
        self.genre = genre

    # Method to print a video information like title, storyline etc.,
    def show_info(self):
        print("Title: " + self.title)
        print("storyline: " + self.storyline)
        print("genre:" + self.genre)
