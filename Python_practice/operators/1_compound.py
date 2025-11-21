import stdio
import sys
import math

# save variables to plug into formula
t = float(sys.argv[1])
p = float(sys.argv[2])
r = float(sys.argv[3])
e = math.e

# if r is not given as decimal ask user to input a decimal instead
if r > 1:
    stdio.writeln("Interest rate should be a decimal (example: 0.1 for 10%). You entered: " + str(r))
    sys.exit("Retry execution with decimal r")

# given compounding formula from textbook
compounded = p * ((e)**(r * t))

# print out the compounded amount of money
stdio.writeln("Compounded result of $" + str(p) + " at " + str(r*100) + "% interest rate for " + str(t) + " years: $" + str(compounded))