
class Video(object):
    def __init__(self, title,storyline, genre):
         self.title = title
         self.storyline = storyline
         self.genre = genre

    def show_info(self):
         print("Title: "+ self.title)
         print("storyline: "+ self.storyline)
         print("genre:"+ self.genre)
