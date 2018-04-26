import fresh_tomatoes
import media

#Create instances of Movies.
toy_story = media.Movies("Toy Story", "This is a movies about toys",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg")

thor = media.Movies("Thor"," A hammer that only thor can lift",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcRSZN3c1Wj6s6Nz0DLOYTZY4GM27rt6zRDCdw_z_0ff8oAKTeXE")

wonder_woman = media.Movies("Wonder Woman", "In Wonder Woman, the story of Diana is told,who is the daughter of Hippolyta",
                           "https://youtu.be/VSB4wGIdDwo",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H")

source_code = media.Movies("Source Code", " It is a movie about the potential of technology","https://www.youtube.com/watch?v=NkTrG-gpIzE",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgKtKKeXjHx0L8Ii8jJfWr16rzIu9TYmQdIXDxtMJXOMN-ihegByzIZQ")

moana = media.Movies("Moana", "Is a 3d movie focusing around adventure", "https://www.youtube.com/watch?v=LKFuXETZUsI",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser_Poster.jpg")

hunger_games= media.Movies("Hunger Games", "Focusing around the reality of Life how human race is controlled by the superiors",
                             "https://www.youtube.com/watch?v=mfmrPu43DF8",
                             "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg")

three_idiots= media.Movies("Three Idiots",
                           " A movie which focuses on the education and thinking level of the society's educated people and tries to change it ",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg")

#keeping all instance of Movies in a list
movies_list=[thor, wonder_woman, source_code, moana,hunger_games, three_idiots]

#Passing the list to the funciton to generate HTML page
fresh_tomatoes.open_movies_page(movies_list)




