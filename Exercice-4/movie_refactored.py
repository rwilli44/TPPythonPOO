import json
from datetime import datetime, date
from os import path


class Movie:
    movie_collection = []
    json_file = "./Exercice-4/movie_collection.json"
    def __init__(self, title: str, release_date: str, summary: str) -> None:
        self.__title = title.title() # .title() ensures that the title is saved in Title Case
        self.__summary = summary 
        
         # verifies release date format - this is redundant if a Movie instance is made through the factory
         # but is necessary if an instance is made directly from using Movie(). It is worth keeping it in the
         # factory as well as it stops the user from writing out a summary if they have used an incorrect date
        if Movie.verify_date(release_date):
            self.__release_date = release_date
        
        # self.json_add_movie() # Calls the function to add the new movie to the JSON file
        self.movie_collection.append(self)
        
    def __str__(self):
        return f"{self.__title}, {self.__release_date}\n{self.__summary}"

#### Instance Method(s)
    @classmethod
    def update_json(cls):
        """When a new movie is added or an existing movie is updated or deleted, this function writes the new 'cls.movie_collection' to JSON.
        """
        try:
            with open(cls.json_file, "w") as f:
                new_movie_collection = {"movies": []}
                for movie in cls.movie_collection:
                    new_movie_collection['movies'].append(movie.__dict__)
                json.dump(new_movie_collection, f, indent=4) 
        except:
            print("\nThere was an error writing to the JSON file. Check that the file hasn't been deleted by accident or contact the developer to report the error.\n")  
      
######################################## Class Methods Necessary for Creating Movie Instances ########################################

    @classmethod
    def add_movies_from_JSON(cls):
        try:
            with open(cls.json_file, "r+") as f:
                json_movies = json.load(f) # copy the existing movie collection to a python format
                for i, movie in enumerate(json_movies["movies"]):
                    Movie(movie['_Movie__title'], movie['_Movie__release_date'],movie['_Movie__summary'])
        except FileNotFoundError:
            print("\nNo JSON file for the movie collection was found. If you believe this is an error, contact the developer.\nOtherwise, maybe you would like to add a movie to the collection ?\n")
        except json.JSONDecodeError: 
            print("\nThe JSON file for the movie collection is currently empty. If you believe this is an error, contact the developer.\nOtherwise, maybe you would like to add a movie to the collection ?\n")
            
        
    @classmethod
    def movie_factory(cls) -> object:
        """Class method to create new instances of Movie based on interactive user input.
        Verifies the date format and returns None if it is invalid and prints error message.

        Returns:
            Movie: an instance of the Movie class if input is valid
        """
        movie_title = input("\nWhat is the title of the movie?\nTitle: ")
        movie_date = input("\nWhat is the release date?\nFormat DD/MM/YYYY: ")
        if not Movie.verify_date(movie_date): # Verify that the date format is correct and it is in an expected range of dates
            return None
        movie_summary = input("\nPlease provide a brief summary of the movie (No Spoilers!).\nSummary: ")
        Movie(movie_title,movie_date,movie_summary)
        Movie.update_json()
        return True    
    
    
    @classmethod
    def verify_date(cls,release_date: str) -> bool:
        """Verifies that the provided release date is the correct DD/MM/YYYY format and is within
        the expected range of dates (14/10/1888 when the first film was released to one year from
        the current date to allow for upcoming features to be included.)

        Args:
            release_date (str): a string in DD/MM/YYYY format

        Returns:
            bool: True if date is in the expected range and the format is valid
        """
        date_format = '%d/%m/%Y'
        try:
            today = date.today()
            latest_date = today.replace(today.year +1) # a date object representing one year from the current date to serve as a date limit
            given_date = datetime.strptime(release_date, date_format).date() # convert user input from a string to a date object
            earliest_date = date(1888,10,14) # date the first film was released
            
            if given_date > latest_date: # date is too far in the future
                print("\nAre you sure about that date? It's more than a year in the future! Please try again.")
                return False
            elif given_date < earliest_date: # date is too far in the past
                print("A\nre you sure about that date? It's before the first known film, 'Roundhay Garden Scene' by Louis Le Prince, was released on 14/10/1888. Please try again.")
                return False
            else: # date is in expected range
                return True
        except ValueError: # attempting to convert an invalid DD/MM/YYYY string to a datetime object raises a ValueError
            print("Invalid input. Please make sure your date respects the proper format: DD/MM/YYYY.")
            return False
        
    @classmethod    
    def verify_json_exists(cls) -> bool:
        """Verifies that json file exists and has at least one entry. The size 91 represents the minimum size possible for a file with one entry if both the title and summary are empty strings. This is done so that if a file is begun by error but an entry is not completed, the file is overwritten to avoid an error upon reading it.

        Returns:
            bool: True if file exists and has at least one entry, False otherwise
        """
        if path.isfile(cls.json_file) and path.getsize(cls.json_file) > 91:
            return True
        else:
            return False
    
######################################## Other Class Methods in Alphabetical Order ########################################
    
    @classmethod
    def delete_movie(cls):
        target_movie = Movie.get_movie_for_UD("delete")
        if target_movie is None:
            return None
        cls.update_json()
        print(f"\n{target_movie._Movie__title} released on {target_movie._Movie__release_date} was successfully removed from the collection.")
        Movie.show_all_movies()
    
    @classmethod
    def get_movie_for_UD(cls,operation):
        print(f"\nSearch for the movie you would like to {operation}.")
        search_results = Movie.search_movie()
        if len(search_results) == 0:
            return None
        elif len(search_results) > 1:
            movie_selected = input(f"\nPlease select the number for the movie you wish to {operation}.\nChoice : ")
            try:
                movie_selected = int(movie_selected)
            except ValueError:
                print(f"\nERROR : Invalid input. Please enter only the number (1, 2, 3...) of the film you wish to {operation}.")
                return None
            if movie_selected not in range(1,len(search_results)+1):
                    print("\nInvalid input. The number you entered does not correspond to a film in the list. Please try again.\n")
                    return None
            else:
                target_movie = search_results[movie_selected-1]
        else:
            target_movie = search_results[0]
        confirmation = input(f"\nAre you sure you want to {operation} {target_movie._Movie__title} released on {target_movie._Movie__release_date} ?\n\nType Y to confirm your choice or any other character to return to the main menu.\nConfirmation ? ")
        if confirmation.lower() != 'y':
            return None
        cls.movie_collection.remove(target_movie)

        return target_movie
    
    @classmethod
    def search_movie(cls):      
        results = [] 
        if len(cls.movie_collection) == 0:
            print("\nSorry, there are not any files in our collection yet.\n")
        else:
            search_term = input("Enter the title you would like to find.\nTitle: ")
            print("\nSearch results: \n")
            try:
                date_format = '%d/%m/%Y'
                sorted_movie_collection = sorted(cls.movie_collection, key=lambda x: datetime.strptime(x._Movie__release_date, date_format))
            except:
                sorted_movie_collection = cls.movie_collection
                print("\nSorry the movies aren't in chronological order, one of the dates is an incorrect format. Please inform the developer so this can be corrected!\n")
            i = 1
            for movie in sorted_movie_collection:
                if search_term.lower() in movie._Movie__title.lower():
                    results.append(movie)
                    print(f"\n{i} : {movie.__str__()}")
                    i+=1
            if len(results) == 0:
                print("Sorry, no results matched your search terms. We may not have that title in our collection.") 
        return results
    
    @classmethod
    def show_all_movies(cls):
        
        if not Movie.verify_json_exists():
            print("\nSorry, there are not any files in our collection yet.\n")
        else:
            date_format = '%d/%m/%Y'
            print("\nThe following movies are in our collection: \n")
            with open(cls.json_file, "r") as f:
                movie_collection = json.load(f)
            try:
                sorted_movie_collection = sorted(movie_collection["movies"], key=lambda x: datetime.strptime(x['_Movie__release_date'], date_format))
            except:
                sorted_movie_collection = movie_collection["movies"]
                print("\nSorry the movies aren't in chronological order, one of the dates is an incorrect format. Please inform the developer so this can be corrected!\n")
            for movie in sorted_movie_collection:
                print(f"{movie['_Movie__title']}, {movie['_Movie__release_date']}\n{movie['_Movie__summary']}\n")    
        
    @classmethod
    def update_movie(cls):
        target_movie = Movie.get_movie_for_UD("update")
        if target_movie is None:
            return None
        
        selected_section = input(f"\nWhat part of the movie information would you like to edit? Enter the corresponding number.\n1 - Title: {target_movie._Movie__title}\n2 - Release Date: {target_movie._Movie__release_date}\n3 - Summary: {target_movie._Movie__summary} \nChoice: ")
        match selected_section:
            case "1":
                new_info = input("Enter the new title: ")
                confirm_change = input(f"The new title is '{new_info}'. Is this correct?\nY/N: ")
                if confirm_change.lower() == "y":
                    target_movie._Movie__title = new_info
            case "2":
                new_info = input("Enter the new release date in the format DD/MM/YYYY: ")
                if Movie.verify_date(new_info):
                    confirm_change = input(f"The new release date is '{new_info}'. Is this correct?\nY/N: ")
                    if confirm_change.lower() == "y":
                        target_movie._Movie__release_date = new_info
                else:
                    confirm_change = "No"
            case "3":
                new_info = input("Enter the summary. Remember, No Spoilers!\nSummary:  ")
                confirm_change = input(f"The new summary is '{new_info}'. Is this correct?\nY/N: ")
                if confirm_change.lower() == "y":
                    target_movie._Movie__summary = new_info
            case _:
                print("Invalid input. Try again and be careful to only enter one choice of section to edit (1,2 or 3)") 
                confirm_change = "No"
        if confirm_change.lower() == "y":
            Movie(target_movie._Movie__title, target_movie._Movie__release_date, target_movie._Movie__summary)
            cls.update_json()
            print(f"\nUpdate Successful:\n\n{target_movie._Movie__title}, {target_movie._Movie__release_date}\n{target_movie._Movie__summary}\n")
        else:
            cls.movie_collection.append(target_movie)
        
        
    
    
        
    
    
    

        
        
    
    
    
    
