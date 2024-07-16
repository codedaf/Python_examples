""" 
Currency Converter

 Simple Python script for converting US dollars to euros, using a fixed exchange rate of 0.95. 
 The script will prompt the user to input an amount in dollars and then convert it to euros.

"""
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month   
year = now.year
hour = now.hour
# Function to convert dollars to euros
exchange_rate=0.95
def convert_dollars_to_euros(dollars):
    euros = dollars * exchange_rate
    return euros
# Main function to handle user input and display the result
def main():
    try:
        # Prompt the user to enter the amount in dollars
        dollars = float(input("Enter the amount in dollars to convert: "))
        # Convert the dollars to euros
        euros = convert_dollars_to_euros(dollars)
        # Display the result
        welcome = "--- Welcome to the exchange ---"  
        print ("-----------------------------------------------")
        print (welcome )      
        print(f"Current date and time: {day:02d}-{month:02d}-{year} {hour:02d}:00")
        print ("----------------------------------------------")
        print ("Exchange rate: " f"{exchange_rate}")
        print(  f"{dollars} dollars is equivalent to {euros:.2f} euros.")
        print ("----------------------------------------------")
    except ValueError:
        # Handle cases where the input is not a valid number
        print("Please enter a valid number.")


# Entry point of the script
if __name__ == "__main__":
    main()





