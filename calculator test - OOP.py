# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import user interface
from user_interface import UserInterface
from calculations import Calculator

u_interface = UserInterface()
calc = Calculator()

# import Calculator
# Ask user for mathematical operations to be used
operation = u_interface.math_operation()

# Ask user for two numbers
num_1 = u_interface.user_input()
num_2 = u_interface.user_input()

# Perform calculations
add = calc.use_operation(operation, num_1= float(), num_2= float())
sum = u_interface.display_sum(add)

# Display result