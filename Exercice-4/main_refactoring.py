from movie_refactored import Movie
import os

def main():
    """
    This function runs the movie database program.
    A while loop continues until the user chooses to exit the program.
    """
    
    # if a JSON file with valid data exists, the movie objects will be created 
    # and saved to memory
    Movie.add_movies_from_JSON() 
    
    # For test purposes only, this will show that although the JSON has 10 entries,
    # the duplicate entry will not load. However, if two entries have the same title and year
    # but different summaries, the second entry will be lost when the JSON file is overwritten 
    # if a movie is created, updated or deleted
    print(f"\n{len(Movie.movie_collection)} movies were loaded from the JSON file.\n")
    
    
    while True:
        
        user_action = input("\nWhat would you like to do ?\n1 - Add a movie to the collection\n2 - Search for a movie\n3 - Browse the entire collection\n4 - Update a movie\n5 - Delete a movie\n6 - Exit\nChoice: ")
        
        match user_action:
            case "1": # Add a movie to the collection 
                new_movie = Movie.create_movie() 
                if new_movie: # if there was an error adding a new movie, the collection won't display
                    Movie.show_all_movies()
            case "2": # Search for a movie
                Movie.search_movie()
            case "3": # Browse the entire collection
                Movie.show_all_movies()
            case "4": # Update a movie
                Movie.update_movie()
            case "5": # Delete a movie
                Movie.delete_movie()
                Movie.show_all_movies()
            case "6": # Exit the program
                print("\nExiting the program. Goodbye!\n")
                exit()
            case _: # Invalid input returns the user to the beginning of the loop to choose again
                print("\nERROR: Please enter enter only the number corresponding to your choice (1-6).")
                        
main()


