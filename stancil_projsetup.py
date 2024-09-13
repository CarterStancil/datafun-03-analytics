''' This module provides functions for creating a series of project folders. '''

#####################################
# Import Modules at the Top
#####################################

# Import modules from standard library
import pathlib
import os
import time

# Import local modules
import utils_stancil

#Declare time for folder counter while loop 
duration_secs = 5

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders in range of years
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    start_year = 2020
    end_year = 2025

    for year in range(start_year, end_year + 1):
        folder_name = f"{year}"
        os.makedirs(folder_name, exist_ok=True)
        print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")





  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
#####################################

folder_id = ['data-csv', 'data-excel', 'data-json']
to_lowercase = True
remove_spaces = True

def create_folders_from_list(folder_list: list) -> None:
    for folder_id in folder_list:
        if to_lowercase == True:
            folder_id = folder_id.lower()
        if remove_spaces== True:
            folder_id = folder_id.replace(' ', '_')
            folder_path = project_path.joinpath(str(folder_id))
            folder_path.mkdir(exist_ok=True)
print(f"Function Called: create_folders_from_list with '{folder_id}'")



  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    folder_id = ['csv', 'excel', 'json']
    prefix = 'data-'
    for folder_id in folder_list:
        folder_path = project_path / f"{prefix}--{folder_id}"
        folder_path.mkdir(exist_ok=True)
print(f"Function Called: create_folders_from_list with '{folder_id}'")

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    folder_count = 0
    number_of_folders = 5

    while folder_count < number_of_folders:
        folder_path = project_path.joinpath(f"folder_{folder_count}")
        folder_path.mkdir(exist_ok=True)
        print(f"Created Folder: {folder_path}")
        time.sleep(duration_secs)
        folder_count += 1



  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_stancil.get_byline()}")


    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2025)


    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)


    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)


    # Call function 4 to create folders periodically using while
    duration_secs:int = 5 
    number_of_folders = 5
    create_folders_periodically(duration_secs)
 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
