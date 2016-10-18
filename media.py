# This piece of code defines the data structure with the class Movie
# instaces created with it will take a set of parameters required by the website generator (fresh_tomatoes)
class Movie():

    """This class defines a data structure that will be used as the core element of a movie database.
    Every entry of the database will require its own instance of the class.
    The fields of the database will be covered by the arguments of the class, listed below

    Atributes:
    title (str): Title of the movie
    storyline (str): Basic description of the movie
    poster_image_url (str): String containing URL to a image of the movie original poster.
    trailer_youtube_url (str): String containing URL to the original trailer in youtube
    """

    def __init__(self, movie_title, movie_storyline,poster_image,trailer_youtube):
        """construstor. It will generate the instances and its attributes
        according to the arguments given
        Args:
        movie_title: will set the title attribute of the instance
        movie_storyline: will set the storyline attribute of the instance
        poster_image: will set the poster_image_url attribute of the instance
        trailer_youtube: will set the trailer_youtube_url attribute of the instance

        all arguments are required when creating the instances

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
