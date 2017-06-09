import media
import fresh_tomatoes

# Movie instances
wonder_woman = media.Movie("Wonder Woman", "A Story of Amazon princess",
                           "http://bit.ly/2r3GjxC",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
                           "Fantasy")
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://bit.ly/2rX0PPD",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io", "Action")
school_of_rock = media.Movie("School of Rock", "guitarist Dewey Finn's "
                             "Adventure",
                             "http://bit.ly/1E376FU",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "comedy")
ratatouille = media.Movie("Ratatouille", "A rat that appreciates good food",
                          "http://bit.ly/2pm0aa7",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "comedy")
midnight_in_paris = media.Movie("Midnight in Paris", "Novelist vacationing "
                                "in Paris",
                                "http://bit.ly/1MG5PfN",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "Comedy")
hunger_games = media.Movie("Hunger Games", "trilogy of young adult "
                           "dystopian novels",
                           "http://bit.ly/1KKnRuk",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo",
                           "Adventure")

movies = [wonder_woman, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

# Calling frsh tomotoes method to generate HTML page.
fresh_tomatoes.open_movies_page(movies)
