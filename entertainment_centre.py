#This is the piece of code to be execute to start the process of the web generating program
#It requires the data structure called Movie, which is defined in the module media
#it also requires the fresh_tomatoes which will generate the website according to the database content

import media
import fresh_tomatoes



#in the next block of code we generate a number of instances of the Movie class, this will be the content of our database

ghostbusters = media.Movie("Ghostbusters",
                        "4 men agaisnt an evil entity that infected New York",
                        "http://i1239.photobucket.com/albums/ff501/cowbybill/ghostbuster_rerelease_poster.jpg",
                        "https://www.youtube.com/watch?v=vntAEVjPBzQ")
rnr_highschool = media.Movie("RnR High School",
                        "The Ramones save the world (sort of)",
                        "http://www.williamstout.com/news/journal/wp-content/uploads/2013/03/rock-n-roll-high-school-movie-poster-1979-1020168886.jpg",
                        "https://www.youtube.com/watch?v=y1001xArPVk")
airplane = media.Movie("Airplane",
                        "Adventures of an airplane landing",
                        "https://s-media-cache-ak0.pinimg.com/564x/83/22/98/832298be7fc7b0c5336ce61ab63b6d2a.jpg",
                        "https://www.youtube.com/watch?v=07pPmCfKi3U")
spaceballs = media.Movie("Spaceballs",
                        "Rebels defend their freedom in a far away galaxy (sort of)",
                        "https://mygeekblasphemy.files.wordpress.com/2012/02/spaceballs_1987_poster.jpg",
                        "https://www.youtube.com/watch?v=uWVSVgU-I0s")

solaris = media.Movie("Solaris",
                     "Journey to a station orbiting the planet Solaris",
                     "https://www.cinematerial.com/media/posters/sm/75/75rjfssg.jpg?v=146575638",
                     "https://www.youtube.com/watch?v=1Tob56MebI8")

amelie = media.Movie("Amelie",
                     "The story of a girls search for happiness by helping others",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=oWedygCWODY")



#we format the instances of Movie created into a list as it is required by fresh_tomatoes
movies = [ghostbusters,rnr_highschool,airplane,spaceballs,solaris,amelie]

#we run the fresh_tomatoes function that will generate the website according to our database 
fresh_tomatoes.open_movies_page(movies)
