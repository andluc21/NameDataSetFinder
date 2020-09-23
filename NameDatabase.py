# North Seattle College
# Lab Week 7
# Author: Luca Andolina
# Email: luca627@comcast.net

# main function definition
def main():
    # Create an empty dictionary that will eventually hold the data
    user_data = {}

    # Process number data from the file here
    # Go through each line of the file
    # Add the name and associated id to the dictionary
    # as key-value pair such that the key is the name and the value is the id

  
    #This opens the user_data.csv file
    database = open("user_data.csv", "r")

    # Loops through  lines until done
    # For & in loops can be used in any collection of data that ends in new line
    for line in database:
        line = line.rstrip("\n") # Removed trailing new lines
        line_list = line.split(",") # Split line on comma to get list strings
        user_data [line_list[0]] = line_list[1] # Creating the dictionary , # Assign second item in list to dictionary with first item as key 
    database.close()
        
        
    
    # User interface
    keep_running = True

    while keep_running:
        
        # Call display_number_info here:
        display_user_info(user_data)

        # Ask the user if they want to continue:
        user_resp = input("Would you like to check another user? (yes/no): ")

        # Stop running the user interface while loop if the user doesn't want to continue    
        if user_resp == "no":
            keep_running = False

# This funciton prompts the user for a username and displays the ID of that user
# Uses the dictionary to look up the user ID, displays a message with the information
# Displays a message if the username is not in the dictionary
def display_user_info(user_data):
    name = input("Please enter a name to look up: ")
    if name in user_data:
        print("The user ID for", name, "is", user_data[name]) 
    else:
        print("Sorry, the user", name, "does not exist.")        

# Call the main function.
main()
