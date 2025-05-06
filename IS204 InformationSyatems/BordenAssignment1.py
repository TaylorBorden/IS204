'''

Name, class, and date
Taylor Borden 
IS204 8/31/2024

Code Report 

Purpose: 
The script collects information about an aircraft and its last flight, calculates the flight efficiency, and displays the results.

Functionality:

User Input:
Prompts the user to enter the aircraft manufacturer, model year, model name, hours flown on the last flight, and fuel consumed on the last flight.
Converts hours_flown and fuel_consumed to floating-point numbers for accurate calculations.

Calculation:
Computes the flight efficiency by dividing the number of hours flown by the amount of fuel consumed.

Output:
Displays the aircraft's model year, manufacturer, and model name.
Prints the calculated flight efficiency.

Test case:


'''



# Ask for the user to input the following information 
manufacturer = input("1. Enter the aircraft manufacturer: ")
model_year = input("2. Enter the aircraft model year: ")
model_name = input("3. Enter the aircraft model name: ")
hours_flown = float(input("4. Enter the number of hours flown on the last flight: "))
fuel_consumed = float(input("5. Enter the amount of fuel consumed on the last flight (in gallons): "))

# Calculate the flight efficiency by dividing the fuel consumed by the hours flown
flight_efficiency = hours_flown/fuel_consumed

# Display the results
print(model_year, manufacturer, model_name)
print(flight_efficiency)



