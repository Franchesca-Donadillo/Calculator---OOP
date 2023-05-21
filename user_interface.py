# Franchesca Marie U. Donadillo
# BSCPE 1-5

import pyfiglet
from termcolor import colored, cprint

# Create user interface class
class UserInterface:
    # initialize
    def __init__(self):
        title = pyfiglet.figlet_format("MATH OPERATIONS\n", font="cricket")
        print(colored(title.center(55), "magenta", attrs=["bold"]))
        cprint(colored("~ Addition"), "blue", attrs=["bold"])
        cprint(colored("~ Subtraction"), "blue", attrs=["bold"])
        cprint(colored("~ Multiplication"), "blue", attrs=["bold"])
        cprint(colored("~ Division\n"), "blue", attrs=["bold"])

    # Get user's mathematical operation
    def math_operation(self):
        cprint(colored("="*83),"green")
        operation = input("Enter the mathematical operation you want to perform between two numbers: ").upper()
        return operation
    
    # Define function user_input
    def user_input(self, num_name):
        cprint(colored("------"), "cyan")
        num = float(input("Enter" + num_name + "number: "))
        return num

    # Display sum
    def display_sum(self, sum):
        cprint(colored("="*83), "green")
        cprint(colored(f"++ The sum of the numbers is {sum} ++\n"), "cyan", attrs=["bold", "reverse"])

    # Display difference
    def display_diff(self,diff):
        print(colored("="*83), "green")
        cprint(colored(f"-- The difference of the numbers is {diff} --\n"), "cyan", attrs=["bold", "reverse"])
        
    # Display product
    def display_prod(self, prod):
        cprint(colored("="*83), "green")
        cprint(colored(f"×× The product of the numbers is {prod} ××\n"), "cyan", attrs=["bold", "reverse"])

    # Display quotient
    def display_quo(self, quo):
        cprint(colored("="*83), "green")
        cprint(colored(f"÷÷ The quotient of the numbers is {quo} ÷÷\n"), "cyan", attrs=["bold", "reverse"])

    def user_repeat(self, main):
        cprint(colored("="*83), "green")
        repeat = input("Do you want to repeat? yes/no: ")
        print("\n")

        if repeat == "yes":
            main()

        elif repeat == "no":
            thanks = pyfiglet.figlet_format("THANK YOU!", font = "linux")
            cprint(colored(thanks), "yellow")
            exit()

        else:
            print("Invalid. Type yes or no only.\n")
            cprint(colored("="*83), "red")
            repeat = input("Do you want to repeat? yes/no: ")
            print("\n")

            if repeat == "yes":
                main()

            elif repeat == "no":
                thanks = pyfiglet.figlet_format("THANK YOU!", font = "linux")
                cprint(colored(thanks), "yellow")
                exit()



    