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
        operation = input("Enter the mathematical operation you want to perform between two numbers: ").upper()
        return operation
    
    # Define function user_input
    def user_input(self, num_name):
        num = float(input("Enter" + num_name + "number: "))
        return num

    # Display sum
    def display_sum(self, sum):
        print("="*83)
        print("The sum of the numbers is " + str(sum), "\n")

    # Display difference
    def display_diff(self,diff):
        print("="*83)
        print("The difference of the numbers is " + str(diff), "\n")
        
    # Display product
    def display_prod(self, prod):
        print("="*83)
        print("The product of the numbers is " + str(prod), "\n")

    # Display quotient
    def display_quo(self, quo):
        print("="*83)
        print("The quotient of the numbers is " + str(quo), "\n")

    def user_repeat(self, main):
        print("="*83)
        repeat = input("Do you want to repeat? yes/no: ")
        print("\n")

        if repeat == "yes":
            main()

        elif repeat == "no":
            print("THANK YOU!")
            exit()

        else:
            print("Invalid. Type yes or no only.\n")
            print("="*83)
            repeat = input("Do you want to repeat? yes/no: ")
            print("\n")

            if repeat == "yes":
                main()

            elif repeat == "no":
                print("THANK YOU!")
                exit()

    