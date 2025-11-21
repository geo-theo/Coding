from binaryapi import *
from colorapi import *
from color import Color

#################################
###### Testing binaryapi.py #####
#################################
print("------------------")
print("Test binaryapi.py")
print("------------------")
print("")

# empty strings errors
print("Validate for empty strings:")
try:
    integerToBinary("")
except ValueError as e:
    print("integerToBinary caught empty string error:", e)
try:
    integerToBinaryRecursive("")
except ValueError as e:
    print("integerToBinaryRecursive caught empty string error:", e)
try:
    binaryToInteger("")
except ValueError as e:
    print("binaryToInteger caught empty string error:", e)
try:
    addBinary('100','')
except ValueError as e:
    print("addBinary caught empty string error:", e)
try:
    invertBinary("")
except ValueError as e:
    print("invertBinary caught empty string error:", e)
try:
    padBinary('', 4)("")
except ValueError as e:
    print("padBinary caught empty string error:", e)
print("_____")
print("")

# non-string errors
print("Validate for non-strings:")
try:
    binaryToInteger(101)
except ValueError as e:
    print("binaryToInteger caught non-string error:", e)
try:
    addBinary("100", 101)('100','')
except ValueError as e:
    print("addBinary caught non-string error:", e)
try:
    invertBinary(101)
except ValueError as e:
    print("invertBinary caught non-string error:", e)
try:
    padBinary(101, 5)
except ValueError as e:
    print("padBinary caught non-string error:", e)
print("_____")
print("")

# non-integers errors
print("Validate for non-integers:")
try:
    integerToBinary('Hello')
except ValueError as e:
    print("integerToBinary caught non-integer error:", e)
try:
    integerToBinaryRecursive('Hello')
except ValueError as e:
    print("integerToBinaryRecursive caught non-integer error:", e)
try:
    padBinary('101', 'five')
except ValueError as e:
    print("padBinary caught non-integer error:", e)
print("_____")
print("")

# negative integers errors
print("Validate for negative integers:")
try:
    integerToBinary(-1)
except ValueError as e:
    print("integerToBinary caught non-integer error:", e)
try:
    integerToBinaryRecursive(-1)
except ValueError as e:
    print("integerToBinaryRecursive caught non-integer error:", e)
try:
    padBinary('101', -5)
except ValueError as e:
    print("padBinary caught non-integer error:", e)
print("_____")
print("")

# non-0s-1s errors
print("Validate for non-0s-and-1s:")
try:
    binaryToInteger("102")
except ValueError as e:
    print("binaryToInteger caught non-0s-and-1s error:", e)
try:
    addBinary("101", "102")
except ValueError as e:
    print("addBinary caught non-0s-and-1s error:", e)
try:
    invertBinary("102")
except ValueError as e:
    print("invertBinary caught non-0s-and-1s error:", e)
try:
    padBinary("102", 5)
except ValueError as e:
    print("padBinary caught non-0s-and-1s error:", e)
print("_____")
print("")

# integerToBinary
print("Test function integerToBinary:")
print("Should return 0: " + str(integerToBinary(0)))
print("Should return 1: " + str(integerToBinary(1)))
print("Should return 10: " + str(integerToBinary(2)))
print("Should return 110010: " + str(integerToBinary(50)))
print("Should return 101101101: " + str(integerToBinary(365)))
print("_____")
print("")

# integerToBinaryRecursive
print("Test function integerToBinaryRecursive:")
print("Should return 0: " + str(integerToBinaryRecursive(0)))
print("Should return 1: " + str(integerToBinaryRecursive(1)))
print("Should return 10: " + str(integerToBinaryRecursive(2)))
print("Should return 110010: " + str(integerToBinaryRecursive(50)))
print("Should return 101101101: " + str(integerToBinaryRecursive(365)))
print("_____")
print("")

# binaryToInteger
print("Test function binaryToInteger:")
print("Should return 0: " + str(binaryToInteger("0")))
print("Should return 1: " + str(binaryToInteger("1")))
print("Should return 5: " + str(binaryToInteger("101")))
print("Should return 5: " + str(binaryToInteger("000101"))) # test with multiple leading zeroes, should be same as "101" above
print("_____")
print("")

# addBinary
print("Test function addBinary:")
print("Should return 0: " + str(addBinary("0", "0")))
print("Should return 1: " + str(addBinary("0", "1")))
print("Should return 1000: " + str(addBinary("101", "11")))
print("Should return 10000: " + str(addBinary("101", "1011")))
print("_____")
print("")

# isBinaryString
print("Test function isBinaryString:")
print("Should return False: " + str(isBinaryString("")))
print("Should return False: " + str(isBinaryString(101)))
print("Should return True: " + str(isBinaryString("0")))
print("Should return True: " + str(isBinaryString("1")))
print("Should return True: " + str(isBinaryString("0101")))
print("Should return False: " + str(isBinaryString("102")))
print("_____")
print("")

# invertBinary
print("Test function invertBinary:")
print("Should return 1: " + str(invertBinary("0")))
print("Should return 0: " + str(invertBinary("1")))
print("Should return 011: " + str(invertBinary("100")))
print("Should return 0101: " + str(invertBinary("1010")))
print("_____")
print("")

# padBinary
print("Test function padBinary:")
print("Should return 000: " + str(padBinary("0", 3)))
print("Should return 0000000001: " + str(padBinary("1", 10)))
print("Should return 00101: " + str(padBinary("101", 5)))
print("Should return 101: " + str(padBinary("101", 3))) # no need to pad with zeros
print("_____")
print("")

print("+++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++")
################################
###### Testing colorapi.py #####
################################
print("-----------------")
print("Test colorapi.py")
print("-----------------")
print("")

# errors (empty strings and non-colors)
#since all functions use make_color, this is easy way to test for empty strings and non-color errors that are brought up in make_colors()
print("Validate for empty strings:")
try:
    make_color("")
except ValueError as e:
    print("All functions caught empty string error:", e)
print("Validate for non-colors:")
try:
    make_color("Hello")
except ValueError as e:
    print("All functions caught non-color error:", e)
print("_____")
print("")

# luminance
print("Test function luminance:")
print("Black: " + str(luminance("black")))
print("White: " + str(luminance("white")))
print("Crimson: " + str(luminance("crimson")))
print("Should return 124.38: " + str(luminance(Color(57, 138, 231))))
print("_____")
print("")

# isCompatible("red", "") # raise error for empty string
# isCompatible("red", "Hello") # raise error for non-color
# isCompatible("red", 1) # raise error for non-color
# isCompatible
print("Test function isCompatible:")
print("Should return True: " + str(isCompatible("black", "white") ))
print("Should return False: " + str(isCompatible("blue", "purple")))
print("Should return False: " + str(isCompatible("blue", "purple")))
print("Should return True: " + str(isCompatible("cyan", "darkred")))
print("Should return False: " + str(isCompatible((Color(57, 138, 231)), (Color(254, 11, 120)))))
print("_____")
print("")

# print(grayscale("")) # raise error for empty string
# print(grayscale("Hello")) # raise error for non-color
# print(grayscale(1)) # raise error for non-color
# luminance
print("Test function grayscale:")
print("Red grayscale: " + str(grayscale("red")))
print("Yellow grayscale: " + str(grayscale("yellow")))
print("Violet grayscale: " + str(grayscale("violet")))
print("Should return 124, 124, 124: " + str(grayscale(Color(57, 138, 231))))
print("_____")
print("")

# contrastRatio("red", "") # raise error for empty string
# contrastRatio("red", "Hello") # raise error for non-color
# contrastRatio("red", 1) # raise error for non-color
print("Test function contrastRatio:")
print("Should return 21.0: " + str(contrastRatio("black", "white")))
print("Should return 8.73: " + str(contrastRatio("yellow", "navy")))
print("Should return 1.45: " + str(contrastRatio("salmon", "beige")))
print("Should return 1.26: " + str(contrastRatio((Color(57, 138, 231)), (Color(254, 11, 120)))))
print("_____")
print("")

# print(complementary("")) # raise error for empty string
# print(complementary("Hello")) # raise error for non-color
# print(complementary(1)) # raise error for non-color

print("Test function complementary:")
print("Should return 0, 255, 255: " + str(complementary("red")))
print("Should return 0, 0, 255: " + str(complementary("yellow")))
print("Should return 0, 128, 175: " + str(complementary("coral")))
print("Should return 198, 117, 24: " + str(complementary(Color(57, 138, 231))))
print("_____")
print("")