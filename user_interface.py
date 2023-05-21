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
        num = float(input("Enter number: "))
        return num

    # Display sum
    def display_sum(self, sum):
        print("The sum of the numbers is " + str(sum))

    # Display difference
    def display_diff(self,diff):
        print("The difference of the numbers is " + str(diff))
        
    # Display product
    def display_prod(self, prod):
        print("The product of the numbers is " + str(prod))

    # Display quotient
    def display_quo(self, quo):
        print("The quotient of the numbers is " + str(quo))

    def user_repeat(self, main):
        repeat = input("Do you want to repeat? yes/no: ")

        if repeat == "yes":
            main()

        elif repeat == "no":
            print("THANK YOU!")
            exit()

        return repeat