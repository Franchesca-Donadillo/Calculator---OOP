# Franchesca Marie U. Donadillo
# BSCPE 1-5

from termcolor import colored, cprint

from user_interface import UserInterface

class InheritInterface(UserInterface):
    # overwrite the math operation from UserInterface class
    # description changed
    def math_operation(self):
        cprint(colored("="*83),"green")
        operation = input("Enter either the mathematical operation or choose from 1-4 on what you want to perform between two numbers: ").upper()
        return operation
