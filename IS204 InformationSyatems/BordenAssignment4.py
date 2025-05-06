'''

Name, Date, Class
Taylor Borden
10/05/2024 IS204

Code Report:

Purpose: This Python program prompts the user to enter first and last names,
concatenates them in the “last name, first name” format, and writes the names to a file.
The program then opens the file using the default application associated with .txt files.

Key Components:

    1. Variable Initialization:
        fName, lName, wholeName, moreNames, userResponse, nameFile, NameList
        These variables are used to store user input, control the loop, and manage the file name and list of names.

    2. Function Definition:
        concatenate_names(first_name, last_name): This function takes the first and last names as input and returns them in the “last name, first name” format.

    3. User Input:
        The program prompts the user to enter the name of the output file and then repeatedly asks for first and last names until the user indicates they have no more names to add.

    4. File Writing:
        The names are stored in a list (NameList) and then written to a file with the specified name.

    5. File Opening:
        After writing the names to the file, the program uses os.startfile() to open the file on screen.

    6. microsoft copilot assisted in code report and formatting.

Test cases:

Enter the name of the output file: names_list

Please enter the person's first name: Timmy
Please enter the person's last name: Turner
Would you like to enter more names (Y/N)? Y

Please enter the person's first name: Danny 
Please enter the person's last name: Fenton
Would you like to enter more names (Y/N)? N


names_list.txt

    Turner, Timmy
    Fenton, Danny




'''

import os

# Create and initialize the variables 
fName = ""  # First Name
lName = ""  # Last Name
wholeName = ""  # Last name & first name
moreNames = "Yes"  # Loop control variable
userResponse = ""  # User response to whether there are more items
nameFile = ""  # Variable for the output file name
NameList = []  # List object

# Create the function that will concatenate the names
def concatenate_names(first_name, last_name):
    '''Returns the concatenated name in the format: last name, first name'''
    return last_name + ", " + first_name

# Ask the User for the name of the output file they wish to create
nameFile = input("Enter the name of the output file: ")

# Prompt the user to enter a first name and last name and add the names to the list
while moreNames == "Yes":
    fName = input("Please enter the person's first name: ")
    lName = input("Please enter the person's last name: ")
    wholeName = concatenate_names(fName, lName)  # Call the function and place the results in a variable
    NameList.append(wholeName)  # Add name to the list
    userResponse = input("Would you like to enter more names (Y/N)? ")
    if userResponse.upper() == "N":  # Checks the user reply for an N for no by converting to uppercase
        moreNames = "No"

# Open output file. That is, open the file that you have created
nameFile += ".txt"
outputFile = open(nameFile, "w")

# Write list contents to file
for name in NameList:
    outputFile.write(name + "\n")

# Close file
outputFile.close()

# opens text editor to view file 
os.startfile(nameFile)
