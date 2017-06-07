import media
import fresh_tomatoes

wonder_woman = media.Movie("toy story", "Story of a boy and his toys that come to life",
                        "http://bit.ly/2r3GjxC",
                        "https://www.youtube.com/watch?v=1Q8fG0TtVAY", "comic")

avatar = media.Movie("Avatar", "A marine on an alien planet",
               "http://bit.ly/2rX0PPD",
               "http://www.youtube.com/watch?v=-9ceBgWV8io", "Action")
school_of_rock = media.Movie("school_of_rock", "Storyline",
                       "http://bit.ly/1E376FU",
                       "https://www.youtube.com/watch?v=3PsUJFEBC74", "comedy")
ratatouille = media.Movie("ratatouille", "Storyline",
                    "http://bit.ly/2pm0aa7",
                    "https://www.youtube.com/watch?v=c3sBBRxDAqk", "comedy")
midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                    "http://bit.ly/1MG5PfN",
                    "https://www.youtube.com/watch?v=atLg2wQQxvU", "Comedy")
hunger_games = media.Movie("Hunger Games", "StoryLine",
                    "http://bit.ly/1KKnRuk",
                    "https://www.youtube.com/watch?v=PbA63a7H0bo", "Adventure")

movies = [wonder_woman, avatar, school_of_rock, ratatouille,
midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
