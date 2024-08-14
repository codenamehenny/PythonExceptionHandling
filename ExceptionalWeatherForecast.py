#1. Exceptional Weather Forecast
#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

fahrenheit = input("Welcome to the weather forecast application! Here we can convert Fahrenheit to Celsius. \nPlease enter the degrees in Fahrenheit: ")

#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.
#Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

# function that calculates fahrenheit to celsius
def convert_temperature(fahrenheit):
    try:
        fahrenheit = int(fahrenheit) # declares variable as integer to be able to do the math equation
        celsius = (fahrenheit - 32) * 5/9
        celsius = round(celsius, 2) # rounds to 2 decimal places for cleaner look
    except (TypeError, ValueError): # incase user types out actual word instead of the number
        print("Looks a valid digit wasn't entered. Let's try again with digits this time")
    else: # task 3
        print(f"{fahrenheit}°F is equal to {celsius}°C") # displays conversion result
    finally: # task 4 
        print("Thanks for using the weather forecast application! Have a great day")

#calls conversion function
convert_temperature(fahrenheit)

