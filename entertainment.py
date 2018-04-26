import fresh_tomatoes
import media

# Create instances of Movies.
toy_story = media.Movies(
                        "Toy Story", "This is a movies about toys.",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc",
                        "https://goo.gl/MznQRw"
                        )

thor = media.Movies(
                    "Thor", " A hammer that only thor can lift.",
                    "https://www.youtube.com/watch?v=ue80QwXMRHg",
                    "https://goo.gl/87BUrD"
                    )

wonder_woman = media.Movies(
                            "Wonder Woman",
                            "In Wonder Woman, the story of Diana is told.",
                            "https://youtu.be/VSB4wGIdDwo",
                            "https://goo.gl/25tuJo"
                            )


source_code = media.Movies(
                           "Source Code",
                           " It is a movie about the potential of technology.",
                           "https://www.youtube.com/watch?v=NkTrG-gpIzE",
                           "https://goo.gl/RKqkWW"
                           )

moana = media.Movies(
                    "Moana", "Is a 3d movie focusing around adventure.",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI",
                    "https://goo.gl/YqdSU2"
                    )

hunger_games = media.Movies(
                           "Hunger Games",
                           "Focusing around the reality of Life.",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8",
                           "https://goo.gl/4rTAFA"
                           )

three_idiots = media.Movies(
                           "Three Idiots",
                           "A movie which focuses on the education.",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w",
                           "https://goo.gl/WVcKEc"
                            )

# List for storing instances of Movies.
movies_list = [
              thor, wonder_woman, source_code,
              moana, hunger_games, three_idiots
              ]

# Passing the list to the funciton to generate HTML page
fresh_tomatoes.open_movies_page(movies_list)
