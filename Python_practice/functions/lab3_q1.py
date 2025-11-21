### 2.1.1 ###
######################################################################################################
### Compose a function max3() that takes three int or float arguments and returns the largest one. ###
######################################################################################################
import stdio
import sys

def max3(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

number1 = float(sys.argv[1])
number2 = float(sys.argv[2])
number3 = float(sys.argv[3])

stdio.writeln(max3(number1,number2,number3))