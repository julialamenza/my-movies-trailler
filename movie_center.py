import media
import fresh

# movies instance
book_thief = media.Movie("The book thief",
                         " little girl Liesel is separated from her parents and is forced to live with her",
                         "https://upload.wikimedia.org/wikipedia/pt/f/f3/A-Menina-que-Roubava-Livros-poster.jpg",
                         "https://youtu.be/J24AlOYHpVU")

black_swan = media.Movie("Black swan",
                     "A committed dancer wins the lead role in a production of Tchaikovsky's",
                     "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",
                     "https://youtu.be/5jaI1XOB-bs"
                     )
lion_king = media.Movie("Lion King",
                         "A lion life",
                         "https://i.pinimg.com/originals/84/b3/e5/84b3e5d493fc5820a8311bc3b5210db2.jpg",
                         "http://www.youtube.com/watch?v=qe7Qp7VDce0"
                        )
interview_vampire = media.Movie("Interview with the Vampire",
                                "A vampire tells his epic life story",
                                 "https://cdn.cinematerial.com/p/500x/r6mmxhgj/interview-with-the-vampire-movie-cover.jpg",
                                 "https://youtu.be/bDH7P0qvSMU")
#array list to movies list
movies = [book_thief, black_swan, lion_king, interview_vampire]
fresh.open_movies_page(movies)
