# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import user interface
from user_interface import UserInterface
from calculations import Calculator

u_interface = UserInterface()
calc = Calculator()

# import Calculator
# Ask user for mathematical operations to be used
user_operation = u_interface.math_operation()

# Ask user for two numbers
num_1 = u_interface.user_input()
num_2 = u_interface.user_input()

# Perform calculations
# sum = calc.add(num_1= float(), num_2= float())
diff = calc.sub(num_1 = float(), num_2 = float())

# Display result
# sum_display = u_interface.display_sum(sum=float())
display_diff = u_interface.display_diff(diff)
