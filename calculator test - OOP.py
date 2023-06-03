# Franchesca Marie U. Donadillo
# BSCPE 1-5

def main():
 
    # import user interface
    from termcolor import colored, cprint
    from user_interface import UserInterface
    from u_interface_inherit import InheritInterface

    # import Calculator
    from calculations import Calculator

    u_interface = UserInterface()
    calc = Calculator()
    inherit = InheritInterface()

    while True:
        u_interface.design()
        # Ask user for mathematical operations to be used
        user_operation = inherit.math_operation().upper()

        if user_operation != "ADDITION" and user_operation != "1" and user_operation != "SUBTRACTION" and user_operation != "2" and user_operation != "MULTIPLICATION" and user_operation != "3" and user_operation != "DIVISION" and user_operation != "4" and user_operation != "":
            cprint(colored("_"*83), "red")
            cprint(colored("Invalid input.\nCheck your spelling"), "red", attrs=["bold"])
            u_interface.user_repeat(main)          
       
        while True:
            try:
                # Ask user for two numbers
                num_1 = float(u_interface.user_input(" first "))
                num_2 = float(u_interface.user_input(" second "))

                # Perform calculations
                if user_operation == "ADDITION" or user_operation == "1":
                    sum = calc.add(num_1, num_2)
                    # Display resultof addition
                    u_interface.display_sum(sum)

                elif user_operation == "SUBTRACTION" or user_operation == "2":
                    diff = calc.sub(num_1, num_2)
                    # Display result of subtraction
                    u_interface.display_diff(diff)

                elif user_operation == "MULTIPLICATION" or user_operation == "3":
                    prod = calc.multiply(num_1, num_2)
                    # Display result of multiplication
                    u_interface.display_prod(prod)

                elif user_operation == "DIVISION" or user_operation == "4":
                    quo = calc.div(num_1,num_2)
                    # Display result of division
                    u_interface.display_quo(quo)
            
            except ValueError:
                cprint(colored("_"*83), "red")
                cprint(colored("Invalid value. Enter numbers only.\n"), "red", attrs=["bold"])

            except ZeroDivisionError:
                cprint(colored("_"*83), "red")
                cprint(colored("Invalid. You are dividing by 0.\n"), "red", attrs=["bold"])

            finally:
                # ask user if they want to repeat
                u_interface.user_repeat(main)

main()
