# Franchesca Marie U. Donadillo
# BSCPE 1-5

import pyfiglet
from termcolor import colored, cprint
from user_interface import UserInterface

class InheritInterface(UserInterface):
    # overwrite design add other math operations
    def design(self):
        title = pyfiglet.figlet_format("MATH OPERATIONS\n", font="cricket")
        op_1 = "(1)"
        op_2 = "(2)"
        op_3 = "(3)"
        op_4 = "(4)"
        op_5 = "(5)"
        op_6 = "(6)"
        print(colored(title.center(55), "magenta", attrs=["bold"]))
        cprint(colored(f"~ Addition { op_1.rjust(15)}"), "blue", attrs=["bold"])
        cprint(colored(f"~ Subtraction {op_2.rjust(12)}"), "blue", attrs=["bold"])
        cprint(colored(f"~ Multiplication {op_3.rjust(9)}"), "blue", attrs=["bold"])
        cprint(colored(f"~ Division {op_4.rjust(15)}"), "blue", attrs=["bold"])
        cprint(colored(f"~ Power {op_5.rjust(18)}"), "blue", attrs=["bold"])
        cprint(colored(f"~ GCD {op_6.rjust(20)}\n"), "blue", attrs=["bold"])

    # overwrite the math operation from UserInterface class
    # description changed
    def math_operation(self):
        cprint(colored("="*83),"green")
        operation = input("Enter either the mathematical operation or choose from 1-4 on what you want to perform between two numbers: ").upper()
        return operation

    def display_power(self, exp):
        cprint(colored("="*83), "green")
        cprint(colored(f"** The power of the numbers is {exp} **\n"), "cyan", attrs=["bold", "reverse"])

    def display_gcd(self, gcd):
        cprint(colored("="*83), "green")
        cprint(colored(f"** The greatest common factor of the numbers is {gcd} **\n"), "cyan", attrs=["bold", "reverse"])
        