"""
binary.py
Functions for converting between integers and binary strings, including validation and basic binary arithmetic.
"""

def integerToBinary(integerValue):
    """Return the binary string representation of an integer."""
    if not isinstance(integerValue, int):
        raise ValueError("Input must be an integer.")
    if integerValue < 0:
        raise ValueError("Negative integers are not supported.")
    if integerValue == 0:
        return "0"

    binary_digits = []
    while integerValue > 0:
        remainder = integerValue % 2
        binary_digits.append(str(remainder))
        integerValue //= 2

    binary_string = ""
    for bit in reversed(binary_digits):
        binary_string += bit
    return binary_string
# integerToBinary('') # raise error for empty string
# integerToBinary('Hello') # raise error for non-integer
# integerToBinary('1.1') # raise error for non-integer
# integerToBinary(-1) # raise error for negative integer
# integerToBinary(0) # should return 0
# integerToBinary(1) # should return 1
# integerToBinary(2)
# integerToBinary(50)
# integerToBinary(365)

def integerToBinaryRecursive(integerValue):
    """Return the binary string representation of an integer (recursive)."""
    if not isinstance(integerValue, int):
        raise ValueError("Input must be an integer.")
    if integerValue < 0:
        raise ValueError("Negative integers are not supported.")

    if integerValue == 0: #base case for 0
        return "0"
    if integerValue == 1: #base case for 1
        return "1"
    return integerToBinaryRecursive(integerValue // 2) + str(integerValue % 2) #recursive case
# integerToBinaryRecursive('') # raise error for empty string (non-integer)
# integerToBinaryRecursive('Hello') # raise error for non-integer
# integerToBinaryRecursive('1.1') # raise error for non-integer
# integerToBinaryRecursive(-1) # raise error for negative integer
# integerToBinaryRecursive(0) # should return 0
# integerToBinaryRecursive(1) # should return 1
# integerToBinaryRecursive(2)
# integerToBinaryRecursive(50)
# integerToBinaryRecursive(365)

def binaryToInteger(binaryString):
    """Convert a binary string to an integer."""
    if not isinstance(binaryString, str):
        raise ValueError("Input must be a string.")
    if binaryString == "":
        raise ValueError("Input cannot be an empty string.")
    for char in binaryString:
        if char not in ("0", "1"):
            raise ValueError("Binary string can only have '0's and '1's.")

    total = 0
    for bit in binaryString:
        total = total * 2 + int(bit)
    return total
# binaryToInteger('') # raise error for empty string
# binaryToInteger(101) # raise error for non-string
# binaryToInteger("102") # raise error for non 0 or 1 character
# binaryToInteger("0")
# binaryToInteger("1")
# binaryToInteger("101")
# binaryToInteger("000101") # test with multiple leading zeroes, should be same as "101" above

def addBinary(binaryA, binaryB):
    """Add two binary strings and return the sum as binary."""
    if not isinstance(binaryA, str) or not isinstance(binaryB, str):
        raise ValueError("Both inputs must be strings.")
    if binaryA == "" or binaryB == "":
        raise ValueError("Inputs cannot be an empty string.")
    for char in binaryA + binaryB:
        if char not in ("0", "1"):
            raise ValueError("Binary strings can only have '0's and '1's.")

    if len(binaryA) < len(binaryB): # make A same character count as B if A is shorter
        binaryA = ("0" * (len(binaryB) - len(binaryA))) + binaryA
    elif len(binaryB) < len(binaryA): # make B same character count as A if B is shorter
        binaryB = ("0" * (len(binaryA) - len(binaryB))) + binaryB
    max_len = len(binaryA)

    carry = 0
    result = ""
    for i in range((max_len-1), -1, -1): # add from right to left
        bitA = int(binaryA[i])
        bitB = int(binaryB[i])
        total = bitA + bitB + carry
        if total == 0:
            result = "0" + result
            carry = 0
        elif total == 1:
            result = "1" + result
            carry = 0
        elif total == 2:
            result = "0" + result
            carry = 1
        else:
            result = "1" + result
            carry = 1
    if carry == 1: # add remainder carry if any left
        result = "1" + result

    return result
# addBinary('100','') # raise error for empty string
# addBinary("100", 101) # raise error for non-string
# addBinary("101", "102") # raise error for non 0 or 1 characters
# addBinary("0", "0")
# addBinary("0", "1")
# addBinary("1", "1")
# addBinary("101", "11")
# addBinary("101", "1011")

def isBinaryString(value):
    """Return True if the input string only contains '0' and '1'."""
    if not isinstance(value, str):
        return False

    if value == "":
        return False

    for char in value:
        if char not in ("0", "1"):
            return False

    return True
# isBinaryString('') # False
# isBinaryString(101) # False
# isBinaryString("0") # True
# isBinaryString("1") # True
# isBinaryString("101") # True
# isBinaryString("0101") # True
# isBinaryString("102") # False

def invertBinary(binaryString):
    """Return the bitwise inverse of the input binary string."""
    if not isinstance(binaryString, str):
        raise ValueError("Input must be a string.")
    if binaryString == "":
        raise ValueError("Input cannot be an empty string.")
    for char in binaryString:
        if char not in ("0", "1"):
            raise ValueError("Binary string can only have '0's and '1's.")

    inverted = ""
    for char in binaryString:
        if char == "0":
            inverted += "1"
        else:
            inverted += "0"
    return inverted
# invertBinary('') # raise error for empty string
# invertBinary(101) # raise error for non-string
# invertBinary("102") # raise error for non 0 or 1 character
# invertBinary("0")
# invertBinary("1")
# invertBinary("100")
# invertBinary("1010")

def padBinary(binaryString, width):
    """Pad a binary string with leading zeros to reach the given width."""
    if not isinstance(binaryString, str):
        raise ValueError("Input must be a string.")
    if binaryString == "":
        raise ValueError("Input cannot be an empty string.")
    for char in binaryString:
        if char not in ("0", "1"):
            raise ValueError("Binary string can only have '0's and '1's.")
    if not isinstance(width, int):
        raise ValueError("Width must be integer.")
    if width < 0:
        raise ValueError("Width can't be a negative integer.")

    if len(binaryString) >= width:
        return binaryString
    else:
        zeros_to_add = width - len(binaryString)
        padded = ("0" * zeros_to_add) + binaryString
        return padded
# padBinary('', 4) # raise error for empty string
# padBinary(101, 5) # raise error for non-string
# padBinary('101', 'five') # raise error for non-integer
# padBinary('101', -5) # raise error for negative integer
# padBinary("102", 5) # raise error for non 0 or 1 character
# padBinary("0", 3)
# padBinary("1", 10)
# padBinary("101", 5)
# padBinary("101", 3) # no need to pad with zeros