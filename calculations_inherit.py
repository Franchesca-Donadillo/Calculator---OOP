# Franchesca Marie U. Donadillo
# BSCPE 1-5

import math
from calculations import Calculator

class MathOps(Calculator):
    def power(self, num_1, num_2):
        power_op = math.pow(num_1, num_2)
        return power_op
    
    def log(self, num_1, num_2):
        logarithm = math.log(num_1, num_2)
        return logarithm

