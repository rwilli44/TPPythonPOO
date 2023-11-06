import json
from datetime import datetime, date
from os import path


class Movie:
    def __init__(self, title: str, release_date: str, summary: str) -> None:
        self.__title = title.title() # .title() ensures that the title is saved in Title Case
        self.__summary = summary 
        
         # verifies release date format - this is redundant if a Movie instance is made through the factory
         # but is necessary if an instance is made directly from using Movie(). It is worth keeping it in the
         # factory as well as it stops the user from writing out a summary if they have used an incorrect date
        if Movie.verify_date(release_date):
            self.__release_date = release_date
        
        self.json_add_movie() # Calls the function to add the new movie to the JSON file
    

#### Instance Method(s)

    def json_add_movie(self):
        """When a new instance of Movie is created, this function is called by __init__ to add it to the JSON
        file. If the JSON file doesn't exist, a new file is created.
        """
        # calls a class function that returns the path to the JSON file and True if the file already exists with a movie list
        json_file, file_ready = Movie.verify_json_exists()  
        if file_ready:
            with open(json_file, "r+") as f:
                movie_collection = json.load(f) # copy the existing movie collection to a python format
                movie_collection["movies"].append(self.__dict__) # add the new movie to the list
                f.seek(0) # return the pointer to the beginning of the file to overwrite the existing data
                json.dump(movie_collection, f, indent=4) # write the data including the new movie to the JSON file
        else:
            with open(json_file,"w") as f: # if a JSON file with movie data didn't already exist, a new blank file is created
                json.dump({"movies": [self.__dict__]}, f, indent=4) # write the new movie's data to the JSON file in the expected format
      
      
      
######################################## Class Methods Necessary for Creating Movie Instances ########################################

        
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
        return Movie(movie_title,movie_date,movie_summary)    
    
    
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
                print("Are you sure about that date? It's more than a year in the future! Please try again.")
                return False
            elif given_date < earliest_date: # date is too far in the past
                print("Are you sure about that date? It's before the first known film, 'Roundhay Garden Scene' by Louis Le Prince, was released on 14/10/1888. Please try again.")
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
        json_file = "./Exercice-4/movie_collection.json"
        if path.isfile(json_file) and path.getsize(json_file) > 91:
            return json_file, True
        else:
            return json_file, False
    
######################################## Other Class Methods in Alphabetical Order ########################################
    
    @classmethod
    def delete_movie(cls):
        movie_collection, target_movie = Movie.get_movie_for_UD("delete")
        if movie_collection is None:
            return None
        with open("./Exercice-4/movie_collection.json", "w") as f:
            json.dump(movie_collection, f, indent=4)
        print(f"\n{target_movie['_Movie__title']} released on {target_movie['_Movie__release_date']} was successfully removed from the collection.")
        Movie.show_all_movies()
    
    @classmethod
    def get_movie_for_UD(cls,operation):
        print(f"\nSearch for the movie you would like to {operation}.")
        search_results = Movie.search_movie(for_UD=True)
        if len(search_results) == 0:
            return None, None
        elif len(search_results) > 1:
            movie_selected = input(f"Please select the number for the movie you wish to {operation}.\nChoice : ")
            try:
                movie_selected = int(movie_selected)
            except ValueError:
                print(f"\nERROR : Invalid input. Please enter only the number (1, 2, 3...) of the film you wish to {operation}.")
                return None, None
            if movie_selected not in range(1,len(search_results)+1):
                    print("\nInvalid input. The number you entered does not correspond to a film in the list. Please try again.\n")
                    return None, None
            else:
                target_movie = search_results[movie_selected-1]
        else:
            target_movie = search_results[0]
        confirmation = input(f"\nAre you sure you want to {operation} {target_movie['_Movie__title']} released on {target_movie['_Movie__release_date']} ?\n\nType Y to confirm your choice or any other character to return to the main menu.\nConfirmation ? ")
        if confirmation.lower() != 'y':
            return None, None
        with open("./Exercice-4/movie_collection.json", "r+") as f:
                movie_collection = json.load(f)
                for i, movie in enumerate(movie_collection["movies"]):
                    if movie["_Movie__title"] == target_movie["_Movie__title"] and movie["_Movie__release_date"] == target_movie["_Movie__release_date"] and movie["_Movie__summary"] == target_movie["_Movie__summary"]:
                        target_index = i
                        break
        movie_collection["movies"].pop(target_index)
        return movie_collection, target_movie
    
    @classmethod
    def search_movie(cls, for_UD = False):      
        json_file, file_ready = Movie.verify_json_exists()
        results = [] 
        if not file_ready:
            print("\nSorry, there are not any files in our collection yet.\n")
        else:
            search_term = input("Enter the title you would like to find.\nTitle: ")
            print("\nSearch results: \n")
            with open(json_file, "r") as f:
                movie_collection = json.load(f)
            try:
                date_format = '%d/%m/%Y'
                sorted_movie_collection = sorted(movie_collection["movies"], key=lambda x: datetime.strptime(x['_Movie__release_date'], date_format))
            except:
                sorted_movie_collection = movie_collection["movies"]
                print("\nSorry the movies aren't in chronological order, one of the dates is an incorrect format. Please inform the developer so this can be corrected!\n")
            i = 1
            for movie in sorted_movie_collection:
                if search_term.lower() in movie["_Movie__title"].lower():
                    results.append(movie)
                    movie_description = f"{movie['_Movie__title']}, {movie['_Movie__release_date']}\n{movie['_Movie__summary']}\n"
                    if for_UD: 
                        print(f"{i} : {movie_description}")
                        i+=1
                    else:
                        print(movie_description)
            if len(results) == 0:
                print("Sorry, no results matched your search terms. We may not have that title in our collection.") 
        return results
    
    @classmethod
    def show_all_movies(cls):
        json_file, file_ready = Movie.verify_json_exists()
        if not file_ready:
            print("\nSorry, there are not any files in our collection yet.\n")
        else:
            date_format = '%d/%m/%Y'
            print("\nThe following movies are in our collection: \n")
            with open(json_file, "r") as f:
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
        movie_collection, target_movie = Movie.get_movie_for_UD("update")
        if movie_collection is None:
            return None
        
        selected_section = input(f"\nWhat part of the movie information would you like to edit? Enter the corresponding number.\n1 - Title: {target_movie['_Movie__title']}\n2 - Release Date: {target_movie['_Movie__release_date']}\n3 - Summary: {target_movie['_Movie__summary']} \nChoice: ")
        match selected_section:
            case "1":
                new_info = input("Enter the new title: ")
                confirm_change = input(f"The new title is '{new_info}'. Is this correct?\nY/N: ")
                selected_section = "_Movie__title"
            case "2":
                new_info = input("Enter the new release date in the format DD/MM/YYYY: ")
                if not Movie.verify_date(new_info):
                    return None
                confirm_change = input(f"The new release date is '{new_info}'. Is this correct?\nY/N: ")
                selected_section = "_Movie__release_date"

            case "3":
                new_info = input("Enter the summary. Remember, No Spoilers!\nSummary:  ")
                confirm_change = input(f"The new summary is '{new_info}'. Is this correct?\nY/N: ")
                selected_section = "_Movie__summary"

            case _:
                print("Invalid input. Try again and be careful to only enter one choice of section to edit (1,2 or 3)") 
                return None  
                
        if confirm_change.lower() == "y":
            target_movie[selected_section] = new_info
            movie_collection['movies'].append(target_movie)
        else:
            return None                 
        with open("./Exercice-4/movie_collection.json", "w") as f:
            json.dump(movie_collection, f, indent=4)
        
        print(f"\nUpdate Successful:\n\n{target_movie['_Movie__title']}, {target_movie['_Movie__release_date']}\n{target_movie['_Movie__summary']}\n")
    
    
        
    
    
    

        
        
    
    
    
    
