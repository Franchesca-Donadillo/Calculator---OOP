# Franchesca Marie U. Donadillo
# BSCPE 1-5

import math
from calculations import Calculator

class MathOps(Calculator):
    def power(self, num_1, num_2):
        power_op = math.pow(num_1, num_2)
        return power_op
    
    def greatest_cd(self,num_1, num_2):
        gcd = math.gcd(num_1, num_2)
        return gcd

