'''

Name, Date, Class
Taylor Borden
10/03/2024 IS204

Code Report:

Purpose: The script calculates fuel mileage for trips recorded
in a file named “trips.txt” and saves the results to an output file named “output.txt”.

Key Operations:

    1. File Handling:
        Input File: Reads trip data from “trips.txt”.
        Output File: Writes the results to “output.txt”.
    
    2. Data Processing:
        Reads each line from the input file.
        Splits the line into trip date, fuel used, and miles traveled.
        Calculates fuel mileage (miles per gallon).
        
    3. Output:
        Displays the results for each trip.
        Writes the results to the output file with a header.
        
    4. import os:
        used os.startfile() on both files to open on users screen 
        
    5. Error Handling:
        prints an error message if the input file is not found. (check your file location or file name and change if needed).
        
    6. microsoft copilot assisted in code report and formatting.
        
    

Test cases:

"trips.txt" file contents: (No headers, not spaced, not rounded, no fuel mileage calculation, poor visualization of data)
    1-21-2019,12,243
    1-23-2019,15.3,302.4
    1-25-2019,10.9,209.3
    1-31-2019,23.2,543.9
    2-13-2019,15.3,409.3
    
"output.txt" file contents: (Headers made, correctly spaced with commas, rounded 2 decimal places, adds Fuel mileage calculation, better visualization of data)
    Trip Date, Amount of Fuel Used, Numbers of Miles Traveled, Fuel Mileage (mpg)
    1-21-2019, 12.00, 243.00, 20.25
    1-23-2019, 15.30, 302.40, 19.76
    1-25-2019, 10.90, 209.30, 19.20
    1-31-2019, 23.20, 543.90, 23.44
    2-13-2019, 15.30, 409.30, 26.75

'''


import os

# variable creation and initialization
# Hardcoded file names 
input_file_name = "trips.txt"  # the file given to us to read from CANVAS in the directory
output_file_name = "output.txt"  # the new file created with our changes, check your directory

try:
    # Open the input file for reading
    with open(input_file_name, 'r') as infile:
        # Open the output file for writing
        with open(output_file_name, 'w') as outfile:
            # Write a header for the output file
            outfile.write("Trip Date, Amount of Fuel Used, Numbers of Miles Traveled, Fuel Mileage (mpg)\n")
            
            # Read each line from the input file
            for line in infile:
                # Strip newline characters and split the data by commas
                trip_data = line.strip().split(',')
                
                # Assign each item to its appropriate variable
                trip_date = trip_data[0]  # Trip date
                fuel_used = float(trip_data[1])  # Fuel used, converted to float
                miles_traveled = float(trip_data[2])  # Miles traveled, converted to float
                
                # Calculate the fuel mileage for the trip
                fuel_mileage = miles_traveled / fuel_used if fuel_used != 0 else 0
                
                # Display the results for each trip
                print(trip_date + ", Fuel Used: " + format(fuel_used, ".2f") + ", Miles Traveled: " + format(miles_traveled, ".2f") + ", Fuel Mileage: " + format(fuel_mileage, ".2f") + " mpg")
                
                # Write the results to the output file, formatted with commas
                outfile.write(trip_date + ", " + format(fuel_used, ".2f") + ", " + format(miles_traveled, ".2f") + ", " + format(fuel_mileage, ".2f") + "\n")
    
    print("Data successfully saved to " + output_file_name + "!")
    
    os.startfile(input_file_name)
    os.startfile(output_file_name)
    
except FileNotFoundError:
    print("Error: The file '" + input_file_name + "' was not found.")
