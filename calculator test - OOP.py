# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import user interface
from user_interface import UserInterface

# import Calculator
from calculations import Calculator

u_interface = UserInterface()
calc = Calculator()

# Ask user for two numbers
num_1 = float(u_interface.user_input())
num_2 = float(u_interface.user_input())

while True:
    # Ask user for mathematical operations to be used
    user_operation = u_interface.math_operation().upper()

    while True:
        try:
            # Perform calculations
            if user_operation == "ADDITION":
                sum = calc.add(num_1, num_2)
                # Display resultof addition
                sum_display = u_interface.display_sum(sum)

            elif user_operation == "SUBTRACTION":
                diff = calc.sub(num_1, num_2)
                # Display result of subtraction
                display_diff = u_interface.display_diff(diff)

            elif user_operation == "MULTIPLICATION":
                prod = calc.multiply(num_1, num_2)
                # Display result of multiplication
                display_prod = u_interface.display_prod(prod)

            elif u_interface == "DIVISION":
                quo = calc.div(num_1,num_2)
                # Display result of division
                display_quo = u_interface.display_quo(quo)

        except ZeroDivisionError:
            print("Invalid. You are dividing by 0.")

        except ValueError:
            print("Invalid value. Enters numbers only.")

        finally:
            # ask user if they want to repeat
            rep = u_interface.user_repeat()



