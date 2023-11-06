from movie import Movie
import os

def main():
    """A while loop continues until the user chooses to exit the program.
    """
    while True:
        print(os.path.getsize("./Exercice-4/movie_collection.json"))
        user_action = input("\nWhat would you like to do ?\n1 - Add a movie to the collection\n2 - Search for a movie\n3 - Browse the entire collection\n4 - Update a movie\n5 - Delete a movie\n6 - Exit\nChoice: ")
        
        match user_action:
            case "1": # Add a movie to the collection 
                new_movie = Movie.movie_factory()
                if new_movie:
                    Movie.show_all_movies()
            case "2": # Search for a movie
                Movie.search_movie()
            case "3": # Browse the entire collection
                Movie.show_all_movies()
            case "4": # Update a movie
                Movie.update_movie()
            case "5": # Delete a movie
                Movie.delete_movie()
            case "6": # Exit the program
                print("\nExiting the program. Goodbye!\n")
                exit()
            case _: # Invalid input returns the user to the beginning of the loop to choose again
                print("\nERROR: Please enter enter only the number corresponding to your choice (1-6).")
                
            
main()


