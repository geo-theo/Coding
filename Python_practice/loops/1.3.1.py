# Compose a program that takes three integer command-line arguments and writes 'equal' if all three are equal,
# and 'not equal' otherwise.

import stdio
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if num1 == num2 and num1 == num3 and num2 == num3: #we only need two of three equality expressions but this works too
    stdio.write("equal")
else:
    stdio.write("not equal")
