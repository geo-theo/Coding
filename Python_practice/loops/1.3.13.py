# Compose a program that takes a command-line argument n and writes all the positive powers of 2 less than or equal to n.
# Make sure that your program works properly for all values of n. (Your program should write nothing if n is negative or zero.)

import stdio
import sys

n = int(sys.argv[1])

if n <= 0:
    pass # writes nothing if n is zero or negative
else:
    TWO = 2
    x = 0 # starts at 2 to the power of 0, which is 1. So if n=1, then the code would just print out '1'. If n=2, code would print out both 1 and 2. If n=3, code would still just print out 1 and 2. If n=4, code would print out 1, 2, an 4. Etcetera.
    while n >= (TWO ** x): # only run if n is greater than or equal to 2 to the power of x. This includes result of 2 to the power of x when the result is equal to (not just less than) n.
        powered = TWO ** x # 2 to the power of x (keeps increasing as loop runs until we hit n ceiling)
        stdio.writeln(str(powered)) # print result of 2 to the power of wherever x is at with the loop
        x += 1 # keep increasing x that we are powering 2 by until result equals or exceeds n




