 
def km_to_miles(km):
    """
    This function converts kilometers to miles.
    Parameters:
    km (float): Value in kilometers to be converted to miles.
    Return:
    float: Converted value in miles.
    """
    return km * 0.621371

# Ask user to input a value in kilometers
km_input = float(input("Enter the distance in kilometers: "))
# Convert kilometers to miles using the function
miles_output = km_to_miles(km_input)


# Print the result
print(f"{km_input} km is equal to {miles_output} miles")

 

 
