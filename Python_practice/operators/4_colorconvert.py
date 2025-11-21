import stdio
import sys

# instructions say to accept arguments in following order: (1) R, (2) G, (3) B
red = float(sys.argv[1])
green = float(sys.argv[2])
blue = float(sys.argv[3])

# set w as max
maxNum = 255.0
maxW = max((red/maxNum), (green/maxNum), (blue/maxNum))

# if RGB are all 0, then CMYK are all 0 except black
if red==0 and green==0 and blue==0:
    cyan = 0.0
    magenta = 0.0
    yellow = 0.0
    black = 1.0
else:
    # CMYK formulas
    cyan = (maxW - (red/maxNum)) / maxW
    magenta = (maxW - (green/maxNum)) / maxW
    yellow = (maxW - (blue/maxNum)) / maxW
    black = 1.0 - maxW

# print out CMYK values on seperate lines
stdio.writeln("Cyan = " + str(cyan))
stdio.writeln("Magenta = " + str(magenta))
stdio.writeln("Yellow = " + str(yellow))
stdio.writeln("Black = " + str(black))