# Franchesca Marie U. Donadillo
# BSCPE 1-5

# Create user interface class
class UserInterface:
    # initialize
    def __init__(self):
        print("MATHEMATICAL OPERATIONS\n")
        print("~ Addition")
        print("~ Subtraction")
        print("~ Multiplication")
        print("~ Division\n")

    # Get user's mathematical operation
    def math_operation(self):
        operation = input("Enter the mathematical operation you want to perform: ").upper()
        return operation
    
    # Define function user_input
    def user_input(self):
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
        return num_1,num_2

    # Display sum
    # Display difference
    # Display product
    # Display quotient
