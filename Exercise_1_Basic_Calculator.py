"""
Example #1: Basic Calculator
"""
def suma(a, b):
    return a + b

def resta(a, b): 
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Prompt the user to enter the values
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Display the results of the operations
print("Sum:", suma(a, b))
print("Subtraction:", resta(a, b))
print("Multiplication:", multiplicacion(a, b))
print("Division:", division(a, b))


