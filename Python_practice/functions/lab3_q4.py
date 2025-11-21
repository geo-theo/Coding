### 2.1.4 ###
######################################################################################################################
### Compose a function areTriangular() that takes three numbers as arguments and returns True if they could be the ###
### sides of a triangle (none of them is greater than or equal to the sum of the other two), and False otherwise. ###
######################################################################################################################
import stdio
import sys

def areTriangular(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

side1 = float(sys.argv[1])
side2 = float(sys.argv[2])
side3 = float(sys.argv[3])

stdio.writeln(areTriangular(side1,side2,side3))