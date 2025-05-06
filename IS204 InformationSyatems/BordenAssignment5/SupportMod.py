# Taylor Borden 10/18/2024 IS204

"""
Support Module for Trip Data Processing This module contains two functions:

1. Mileage: Calculates the fuel mileage (miles per gallon) for a trip.
2. ItemDisplay: Displays trip data including date, fuel used, miles traveled, and fuel mileage.
"""


# Part 1: Create the Support Module

# Part 1(A): Function to Calculate Fuel Mileage
def Mileage(fuel, miles):
    """
    Calculate the fuel mileage
    
    Parameters:
    fuel (float): The amount of fuel used in gallons.
    miles (float): The number of miles traveled.
    
    Returns:
    float: The calculated fuel mileage (miles per gallon).
    """
    mpg = miles / fuel  # Calculate the fuel mileage
    return mpg  # Return the value

# Part 1(B): Function to Display Trip Data
def ItemDisplay(date, fuel, miles, mileage):
    """
    Display trip data.
    
    Parameters:
    date (str): The date of the trip.
    fuel (float): The amount of fuel used in gallons.
    miles (float): The number of miles traveled.
    mileage (float): The calculated fuel mileage (miles per gallon).
    
    Prints:
    A formatted string displaying the trip date, fuel used, miles traveled, and fuel mileage.
    """
    print ("Trip Date: " + date + "\n" + "Fuel used: " + format(fuel, ".2f")
           + "\n" + "Trip miles: " + format(miles, ".1f")
           + "\n" + "Trip MPG: " + format(mileage, ".2f"))
    return
    

