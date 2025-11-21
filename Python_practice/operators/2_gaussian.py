import stdio
import math
import random

# assign random variables for v and u, using random.random() to generate random real float between 0 and 1
u = random.random()
v = random.random()

#BoxMullerFormula from textbook
z = math.sin(2 * math.pi * v) * ((-2 * math.log(u)) ** (1/2))
#z = math.sin(2 * math.pi * v) * math.sqrt(-2 * math.log(u)) # square root

# print out standard Gaussian random variable
stdio.writeln("Standard Gaussian random variable: " + str(z))