import json
from datetime import datetime, date
from copy import deepcopy
from typing import Self

class Movie:
    """ This class includes Movie objects to store movie data and methods to create, read, update or delete data in the collection by saving to and reading from a JSON file.
    
    Class attributes: movie_collection (list), json_file (str)
    
    Instance attributes: title (str), release_date (str - DD/MM/YYYY)
    """    
    movie_collection = [] # this list will contain all current Movie objects
    json_file = "./Exercice-4/movie_collection.json" 
    
    def __init__(self, title: str, release_date: str, summary: str) -> None:
        self.__title = title.title() # .title() ensures that the title is saved in Title Case
        self.__summary = summary 
        
        # verifies release_date is a valid date in the correct format
        if Movie.verify_date(release_date):
            self.__release_date = release_date
            self.movie_collection.append(self) # keep this in the IF statement to avoid incorrect dates in JSON from causing errors
        
    def __str__(self):
        return f"{self.__title}, {self.__release_date}\n{self.__summary}"
    

######################################## Getters and Setters ########################################

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title.title()

    @property
    def release_date(self) -> str:
        return self.__release_date

    @release_date.setter
    def release_date(self, new_date: str):
        if Movie.verify_date(new_date):
            self.__release_date = new_date

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, new_summary: str):
        self.__summary = new_summary
    
      
######################################## Static Methods Necessary for Creating Movie Instances ########################################
    
    @staticmethod
    def add_movies_from_JSON():
        """Function to be run when the program begins to load data from the JSON file and create objects for any movies already in the collection.
        """
        try:
            with open(Movie.json_file, "r") as f:
                json_movies = json.load(f) 
                for i, movie in enumerate(json_movies["movies"]):
                    # if an entry already exists with the same name and date, the duplicate is not added
                    if not Movie.check_for_duplicates(movie['_Movie__title'], movie['_Movie__release_date']): 
                        Movie(movie['_Movie__title'], movie['_Movie__release_date'],movie['_Movie__summary'])
        except FileNotFoundError:
            print("\nNo JSON file for the movie collection was found. If you believe this is an error, contact the developer.\nOtherwise, maybe you would like to add a movie to the collection ?\n")
        except json.JSONDecodeError: 
            print("\nThe JSON file for the movie collection is currently empty. If you believe this is an error, contact the developer.\nOtherwise, maybe you would like to add a movie to the collection ?\n")
    
    @staticmethod
    def check_for_duplicates(movie_title: str, release_date: str) -> bool:
        """Compares a movie title and release date to those already in the movie collection. 
        Returns True if a duplicate is found.

        Args:
            title (str): title to be added or updated 
            release_date (str): release date to be added or updated DD/MM/YYYY format

        Returns:
            bool: True if a dupublicate is found, False if not
        """
        for movie in Movie.movie_collection:
            if movie_title.lower() == movie.title.lower() and release_date == movie.release_date:
                return True
        return False
            
        
    @staticmethod
    def create_movie() -> bool:
        """Class method to create new instances of Movie based on interactive user input.
        Verifies the date format and checks for duplicates. If there is a duplicate or the date is incorrect,
        the movie is not saved to the collection. If the movie is created, Movie.update_json() is called to
        update the JSON file.

        Returns:
            bool: True if the movie object is created and added to the collection/JSON, False otherwise
        """
        movie_title = input("\nWhat is the title of the movie?\nTitle: ")
        movie_date = input("\nWhat is the release date?\nFormat DD/MM/YYYY: ")
        
        # Verify that the date format is correct and it is in an expected range of dates
        # This seems redundant with the test in __init__, however identifying an incorrect date
        # at this stage saves the user time entering a summary which won't be saved 
        if not Movie.verify_date(movie_date): 
            return False
        if Movie.check_for_duplicates(movie_title, movie_date):
            print(f"\n{movie_title} released on {movie_date} is already in the collection. \nTo change the summary, select 'Update a movie' from the main menu.\n")
            return False
        
        movie_summary = input("\nPlease provide a brief summary of the movie (No Spoilers!).\nSummary: ")
        
        # create the movie object which is automatically added to the movie_collection class attribute list
        Movie(movie_title,movie_date,movie_summary)
        
        # save the updated movie_collection with the new movie to the JSON file
        Movie.update_json()
        return True    
    
    
    @staticmethod
    def verify_date(release_date: str) -> bool:
        """Verifies that the provided release date is the correct DD/MM/YYYY format and is within
        the expected range of dates (14/10/1888 when the first film was released to one year from
        the current date to allow for upcoming features to be included.)

        Args:
            release_date (str): a string in DD/MM/YYYY format

        Returns:
            bool: True if date is in the expected range and the format is valid, False otherwise
        """
        date_format = '%d/%m/%Y'
        try:
            today = date.today()
            latest_date = today.replace(today.year +1) # a date object representing one year from the current date to serve as a date limit
            earliest_date = date(1888,10,14) # date the first film was released
            given_date = datetime.strptime(release_date, date_format).date() # convert the given release date from a string to a date object
            
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
    
    
######################################## Other Class and Static Methods in Alphabetical Order ########################################
    
    @classmethod
    def delete_movie(cls) -> bool:
        """This function allows a user to delete a movie. It calls the function Movie.get_movie_for_UD() 
        passing it the parameter "delete" to allow the user to search for and select the movie they wish to delete. 
        After confirmation, the movie is deleted from the collection and the JSON file is updated by calling Movie.update_json().
        
        Returns: 
            bool: True if successful
        """
        target_movie = Movie.get_movie_for_UD("delete") # returns the Movie object for the movie the user selects
        
        if target_movie is not None:
            cls.movie_collection.remove(target_movie) # remove the object from the movie_collection list 
            cls.update_json() # the new movie_collection list is saved to JSON
            print(f"\n{target_movie.title} released on {target_movie.release_date} was successfully removed from the collection.")
            return True
    
    @staticmethod
    def get_movie_for_UD(operation: str) -> Self:
        """Allows the user to search for the movie they want to update or delete by title and 
        select the correct movie from the returned list of possibilities. Returns the Movie object for 
        the selected movie or None if there was no match or the user did not confirm their choice.

        Args:
            operation (str): a string indicating whether the user is updating ("update") or deleting ("delete") a move. 
            Allows for the user interaction to be adapted to the situation.

        Returns:
            Movie: a Movie object the user has selected to update or delete
        """
        if len(Movie.movie_collection) > 0:
            print(f"\nSearch for the movie you would like to {operation}.")
        
        search_results = Movie.search_movie() # returns a list of all movies matching the user search terms
        
        if len(search_results) == 0: # if no movies matched the user search, returns None
            return None
        elif len(search_results) == 1: # if only one movie is returned it is selected automatically
            target_movie = search_results[0]
        
        # if the search returns more than one result, the user must select the correct movie
        else: 
            movie_selected = input(f"\nPlease select the number for the movie you wish to {operation}.\nChoice : ")
            
            try:
                # if the user has not entered a number, this will raise a Value error and return returns None
                movie_selected = int(movie_selected) 
            except ValueError:
                print(f"\nERROR : Invalid input. Please enter only the number (1, 2, 3...) of the film you wish to {operation}.")
                return None
            
            # if the number selected does not correspond to the search results, returns None
            if movie_selected not in range(1,len(search_results)+1):
                    print("\nInvalid input. The number you entered does not correspond to a film in the list. Please try again.\n")
                    return None
            else:
                target_movie = search_results[movie_selected-1] # 1 is subtracted from the user input to find the correct index
        
        # user is asked to confirm their choice and the selected movie is returned 
        confirmation = input(f"\nAre you sure you want to {operation} {target_movie.title} released on {target_movie.release_date} ?\n\nType Y to confirm your choice or any other character to return to the main menu.\nConfirmation ? ")
        if confirmation.lower() == 'y':
            return target_movie
        else:
            return None
        
    @staticmethod
    def search_movie() -> list:
        """Allows the user to search for a film by title
         
        Returns:
            list: a list of all Movie objects which match the search input
        """
        results = [] 
        
        if len(Movie.movie_collection) == 0:
            print("\nSorry, there are not any files in our collection yet.\n")
            
        else:
            sorted_movie_collection = Movie.sort_by_date() # makes sure search results are ordered oldest to newest
            search_term = input("Enter the title you would like to find.\nTitle: ")
            print("\nSearch results: \n")
            i = 1 # allows the search results to be numbered which is necessary should they be used in an update/delete operation
            for movie in sorted_movie_collection:
                if search_term.lower() in movie.title.lower():
                    results.append(movie) # add the Movie to the results list
                    print(f"\n{i} : {movie.__str__()}") # print the Movie description 
                    i+=1 
            if len(results) == 0:
                print("Sorry, no results matched your search terms. We may not have that title in our collection.") 
        return results
    
    @staticmethod
    def show_all_movies():
        """ Displays all movies in the collection sorted by date from oldest to newest.
        """       
        if len(Movie.movie_collection) > 0:
            print("\nThe following movies are in our collection: \n")
            sorted_movie_collection = Movie.sort_by_date()
            for movie in sorted_movie_collection:
                print(f"{movie}\n")            
        else:
            print("\nSorry, there are not any files in our collection yet.\n")
    
    @staticmethod
    def sort_by_date() -> list:
        """This function sorts the class attribut movie_collection list by date and returns a sorted list to be used when displaying search results or showing all movies.

        Returns:
            list: a copy of the movie_collection sorted by date from oldest to newest.
        """
        try:
                date_format = '%d/%m/%Y'
                # in order to sort by date, the date string for each object is converted into a date() object using the given date_format
                sorted_movie_collection = sorted(Movie.movie_collection, key=lambda x: datetime.strptime(x.release_date, date_format))
        except: # if a movie's date is not in the correct format, it will raise an error and the unsorted list will be returned
                sorted_movie_collection = Movie.movie_collection
                print("\nSorry the movies aren't in chronological order, one of the dates is an incorrect format. Please inform the developer so this can be corrected!\n")
        return sorted_movie_collection

    @staticmethod
    def update_json():
        """When a new movie is added or an existing movie is updated or deleted, this function writes the new 'cls.movie_collection' to JSON.
        """
        try:
            with open(Movie.json_file, "w") as f:
                new_movie_collection = {"movies": []}
                for movie in Movie.movie_collection:
                    new_movie_collection['movies'].append(movie.__dict__)
                json.dump(new_movie_collection, f, indent=4) 
        except:
            print("\nThere was an error writing to the JSON file. Check that the file hasn't been deleted by accident or contact the developer to report the error.\n") 
            
    @classmethod
    def update_movie(cls):
        """This function updates a Movie based on interactive user input. 
        The function only allows for one attribute of a Movie to be changed per call (title, release_date, or summary.)
        """
        target_movie = Movie.get_movie_for_UD("update") # returns a Movie object the user selects
       
        if target_movie is not None:  
            
             # creates a copy of the original data which can be returned if update is abandoned by user choice or invalid input
            copy_target_movie = deepcopy(target_movie) 
            
            # remove the object from the movie_collection list             
            cls.movie_collection.remove(target_movie) 
            
            # select which part of the Movie data will be updated      
            selected_section = input(f"\nWhat part of the movie information would you like to edit? Enter the corresponding number.\n1 - Title: {target_movie.title}\n2 - Release Date: {target_movie.release_date}\n3 - Summary: {target_movie.summary} \nChoice: ")
            
            match selected_section:
                case "1":
                    new_info = input("Enter the new title: ")
                    confirm_change = input(f"The new title is '{new_info}'. Is this correct?\nY/N: ")
                    if confirm_change.lower() == "y":
                        target_movie.title = new_info
                case "2":
                    new_info = input("Enter the new release date in the format DD/MM/YYYY: ")
                    
                    # check that the new date is valid
                    if Movie.verify_date(new_info):
                        confirm_change = input(f"The new release date is '{new_info}'. Is this correct?\nY/N: ")
                        if confirm_change.lower() == "y":
                            target_movie.release_date = new_info
                case "3":
                    new_info = input("Enter the summary. Remember, No Spoilers!\nSummary:  ")
                    confirm_change = input(f"The new summary is '{new_info}'. Is this correct?\nY/N: ")
                    if confirm_change.lower() == "y":
                        target_movie.summary = new_info
                case _:
                    print("Invalid input. Try again and be careful to only enter one choice of section to edit (1,2 or 3)") 
                    
            # check that the update does not create two entries with the same title/date        
            if not Movie.check_for_duplicates(target_movie.title, target_movie.release_date):
                # if no duplicate is found, a new Movie object is created and the JSON file updated
                Movie(target_movie.title, target_movie.release_date, target_movie.summary)
                cls.update_json()
                print(f"\nUpdate Successful:\n\n{target_movie.title}, {target_movie.release_date}\n{target_movie.summary}\n")
            elif Movie.check_for_duplicates(target_movie.title, target_movie.release_date):
                # if a duplicate is found, the copy of the original Movie object is added back to movie_collection and user is informed of the duplicate
                cls.movie_collection.append(copy_target_movie)
                print(f"\n{target_movie.title} released on {target_movie.release_date} was not changed because another movie in the collection has the same title and date. \nPlease verify which entry is correct and delete the duplicate.\n")
            else:
                # if the update is abandoned for any other reason, the copy of the original Movie object is added back to movie_collection
                cls.movie_collection.append(copy_target_movie)
                print(f"\n{target_movie.title} released on {target_movie.release_date} was not changed.\n")
        
    
        
    
    
    
    
