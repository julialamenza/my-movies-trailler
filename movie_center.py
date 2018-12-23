import media
import fresh

# movies instance
book_thief = media.Movie("The book thief",
                         " little girl Liesel is separated from her parents"
                         "and is forced to live with her",
                         "https://bit.ly/2QLQKTf",
                         "https://youtu.be/J24AlOYHpVU")

black_swan = media.Movie("Black swan",
                         "A committed dancer wins the lead role in"
                         "a production of Tchaikovsky's",
                         "https://bit.ly/2V5wGdf",
                         "https://youtu.be/5jaI1XOB-bs")

lion_king = media.Movie("Lion King",
                        "A lion life",
                        "https://movieposters2.com/images/1093584-b.jpg",
                        "http://www.youtube.com/watch?v=qe7Qp7VDce0")

interview_vampire = media.Movie("Interview with the Vampire",
                                "A vampire tells his epic life story",
                                "https://bit.ly/2BDokk3",
                                "https://youtu.be/bDH7P0qvSMU")
# array list to movies list
movies = [book_thief, black_swan, lion_king, interview_vampire]
fresh.open_movies_page(movies)
