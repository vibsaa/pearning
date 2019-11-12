class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")

my_movie=Movie('The Matrix','wachowski')
#Movie.print_info(my_movie)
my_movie.print_info()
