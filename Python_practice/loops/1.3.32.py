# Compose a program that takes a command line argument n and writes all integers less than or equal to n
# that can be expressed as the sum of two cubes in two different ways.
# In other words, find distinct positive integers a, b, c, and d such that a3 + b3 = c3 + d3. Use four nested for loops.

import stdio
import sys

n = int(sys.argv[1])
# four nested loops
for a in range(1, n + 1): # start range at 1 because 0s would provide trivial solutions
    a3 = a**3
    if a3 > n: # if a-cubed is bigger than n we already can't meet the objective since we need a-cubed plus b-cubed to be less than n, so if this is true then break
        break
    for b in range(a, n + 1):
        b3 = b**3
        if a3 + b3 > n: # a-cubed plus b-cubed must be less than n, so if this is true then break
            break
        for c in range(a + 1, n + 1):
            c3 = c**3
            if c3 > a3 + b3: # if c-cubed is bigger than a-cubed + b-cubed we can't meet the objective since c-cubed is too big already
                break
            for d in range(c, n + 1):
                d3 = d**3
                if c3 + d3 > a3 + b3: # this should be equal according to the instructions
                    break
                if c3 + d3 == a3 + b3: # correct equality we are looking for
                    stdio.write(str(a3 + b3) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()




