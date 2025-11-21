### 2.1.19 ###
###########################################################################################################################
### Compose a function any() that takes an array of booleans as its argument and returns True if any of the entries ###
### in the array is True, and False otherwise. Compose a function all() that takes an array of booleans as its argument ###
### and returns True if all of the entries in the array are True, and False otherwise. Note that all() and any() are ###
### Python built-in functions; the goal of this exercise is to understand them better by creating your own versions. ###
###########################################################################################################################
import stdio
import sys

# Return True if ANY element in array is true
def any(values):
    for v in values:
        if v == True:
            return True
        else:
            pass
    return False

# Return True if ALL elements in array are true
def all(values):
    for v in values:
        if v == False:
            return False
        else:
            pass
    return True

# execute functions
input_args_toarray = [arg == "True" for arg in sys.argv[1:]]

any_result = any(input_args_toarray)
all_result = all(input_args_toarray)

stdio.writeln("Any elements true: " + str(any_result) + " | All elements true: " + str(all_result))

