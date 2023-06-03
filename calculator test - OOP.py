# Franchesca Marie U. Donadillo
# BSCPE 1-5

def main():
 
    # import user interface
    from termcolor import colored, cprint
    from user_interface import UserInterface
    from u_interface_inherit import InheritInterface
    from calculations_inherit import MathOps

    # import Calculator
    from calculations import Calculator

    u_interface = UserInterface()
    calc = Calculator()
    inherit = InheritInterface()
    add_ops = MathOps()

    while True:
        inherit.design()
        # Ask user for mathematical operations to be used
        user_operation = inherit.math_operation().upper()

        if user_operation != "ADDITION" and user_operation != "1" and user_operation != "SUBTRACTION" and user_operation != "2" and user_operation != "MULTIPLICATION" and user_operation != "3" and user_operation != "DIVISION" and user_operation != "4" and user_operation != "POWER" and user_operation != "5" and user_operation == "LOG" and user_operation == "6" and user_operation != "":
            cprint(colored("_"*83), "red")
            cprint(colored("Invalid input.\nCheck your spelling"), "red", attrs=["bold"])
            inherit.user_repeat(main)          
       
        while True:
            try:
                # Ask user for two numbers
                num_1 = float(inherit.user_input(" first "))
                num_2 = float(inherit.user_input(" second "))

                # Perform calculations
                if user_operation == "ADDITION" or user_operation == "1":
                    sum = add_ops.add(num_1, num_2)
                    # Display resultof addition
                    inherit.display_sum(sum)

                elif user_operation == "SUBTRACTION" or user_operation == "2":
                    diff = add_ops.sub(num_1, num_2)
                    # Display result of subtraction
                    inherit.display_diff(diff)

                elif user_operation == "MULTIPLICATION" or user_operation == "3":
                    prod = add_ops.multiply(num_1, num_2)
                    # Display result of multiplication
                    inherit.display_prod(prod)

                elif user_operation == "DIVISION" or user_operation == "4":
                    quo = add_ops.div(num_1,num_2)
                    # Display result of division
                    inherit.display_quo(quo)

                elif user_operation == "EXPONENT" or user_operation == "5":
                    exp = add_ops.power(num_1, num_2)
                    # Display result of power
                    inherit.display_power(exp)

                elif user_operation == "LOG" or user_operation == "6":
                    logarithm = add_ops.log(num_1, num_2)
                    # Display result of GCD
                    inherit.display_log(logarithm)
            
            except ValueError:
                cprint(colored("_"*83), "red")
                cprint(colored("Invalid value. Enter numbers only.\n"), "red", attrs=["bold"])

            except ZeroDivisionError:
                cprint(colored("_"*83), "red")
                cprint(colored("Invalid. You are dividing by 0.\n"), "red", attrs=["bold"])

            finally:
                # ask user if they want to repeat
                inherit.user_repeat(main)

main()
