'''
Name, date, and class
Taylor Borden
9/9/2024
IS204

Code Report

Overview
This Python script collects and processes vehicle trip data to calculate and evaluate fuel mileage. 
It allows the user to input details for multiple trips and provides an average fuel mileage at the end.
Additionally, it handles the case where no trips are entered, ensuring the user is not prompted for unnecessary input.

Key Components
User Input for Vehicle Details:
The script prompts the user to enter the car make, model year, and model.
These details are displayed immediately after input.

Initial Prompt for Trips:
The script asks the user if they have any trips to enter before starting the loop.

Loop for Multiple Trips:
The script initializes total_mileage and trip_count to zero.
It enters a while loop to collect trip details if the user has trips to enter.

Trip Details Input:
For each trip, the user inputs the number of miles driven and the amount of fuel used.
The script calculates the fuel mileage for the trip.

Fuel Mileage Evaluation:
The script evaluates whether the vehicle is “Fuel Efficient” (mileage >= 25 miles/gallon) or a “Gas Guzzler” (mileage < 25 miles/gallon).
It displays the calculated mileage and its evaluation.

Updating Totals:
The script updates total_mileage and trip_count for each trip.

Prompt for Additional Trips:
The user is asked if they have more trips to enter. If not, the loop breaks.

Average Mileage Calculation:
After exiting the loop, the script calculates and displays the average mileage if any trips were entered.
If no trips were entered, it informs the user without asking for mileage and fuel.


Test Cases:




'''


# Variable Creation & Initialization

# Collect user input for vehicle details
car_make = input("Enter the car make: ")
car_model_year = input("Enter the car model year: ")
car_model = input("Enter the car model: ")

# Display vehicle details
print(car_model_year, car_make, car_model)

total_mileage = 0
trip_count = 0

# Ask if the user wants to enter a trip
more_trips = input("Do you have any trips to enter? (yes/no): ")

# Start of the loop for multiple trips if the user has trips to enter
while more_trips == 'yes':
    # Collect user input for the trip details
    miles_driven = float(input("Enter the number of miles driven on the last trip: "))
    fuel_used = float(input("Enter the amount of fuel used on the last trip (in gallons): "))
    
    # Calculate fuel mileage
    mileage = miles_driven / fuel_used
    
    # See if our vehicle is 'Fuel Efficient' or a 'Gas Guzzler'
    if mileage >= 25:
        efficiency = "Fuel Efficient"
    else:
        efficiency = "Gas Guzzler"
    
    # Display the fuel mileage and its evaluation
    print("Fuel mileage: ", round(mileage, 2), " miles/gallon - ", efficiency)

    # Update total mileage and trip count for average calculation
    total_mileage += mileage
    trip_count += 1
    
    # Ask if the user wants to enter another trip
    more_trips = input("Do you have any more trips to enter? (yes/no): ")

# Calculate and display the average mileage
if trip_count > 0:
    average_mileage = total_mileage / trip_count
    print("Average mileage: ", round(average_mileage, 2), " miles/gallon")
    print(car_model_year, car_make, car_model, average_mileage)
else:
    print(car_model_year, car_make, car_model)
    print("No trips were entered.")


