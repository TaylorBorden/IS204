# Taylor Borden 10/18/2024 IS204
"""
Main Program for processing Trip Date

This program reads trip data from a file, calculate fuel mileage,
displays the data, and writes the results to a new file.

Steps:
1. Import the Support Module.
2. Initialize Variables.
3. Handle file operations.
4. Process each line from the input file, calculate mileage, display data,
   and write results to the output file.
5. Close the files.

"""

# Part 2: Create the Main Program

# Part 2(A): Import the Support Module
import SupportMod  

# Part 2(B): Initialize Variables
readFileName = "trips"  # variable name for reading the file
writeFileName = "trip_results"  # variable name for creating the file
tripDate = ""  # variable name for the trip date
tripMiles = 0.0  # variable for the trip miles
tripFuel = 0.0  # variable name for the fuel used for the trip
tripMileage = 0.0  # variable name for the calculated trip mileage
commaPosition = 0  # variable for the comma position used in slicing the string
lineLength = 0  # variable name for the length of the file line read

# Part 2(C): File Handling
readFileName += ".txt"  # file extension/format you will be opening
writeFileName += ".txt"  # file extension/format you will be creating

readFile = open(readFileName, "r")  # Open the file to read from it
writeFile = open(writeFileName, "w")  # Open the file to write to it



# Part 2(D): Process and Write Data
for line in readFile:
    commaPosition = line.find(",")  # Find the first comma in the file line read
    lineLength = len(line)  # Get the length of the file line read
    tripDate = line[:commaPosition]  # Extract the first data item from the line read
    line = line[commaPosition + 1: lineLength]  # Slice the line string to remove the first data item
    commaPosition = line.find(",")  # Find the next comma in the line read
    tripFuel = float(line[0:commaPosition])  # Extract the second data item from the line read and convert to float
    tripMiles = float(line[commaPosition + 1:])  # Slice the line string to remove the second data item & assign the last data item

    tripMileage = SupportMod.Mileage(tripFuel, tripMiles)  # Calculate the fuel mileage
    SupportMod.ItemDisplay(tripDate, tripFuel, tripMiles, tripMileage)  # Display the data and calculated items

    writeFile.write(tripDate + ", " + str(format(tripFuel, ".2f")) + ", " + str(format(tripMiles, ".1f")) + ", " + str(format(tripMileage, ".2f")) + "\n")


# close files
readFile.close()
writeFile.close()
