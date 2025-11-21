import stdio
import sys
import math

# instructions say to accept arguments in following order: (1) Central Longitude , (2) Latitude, (3) Longitude
centerLambda = float(sys.argv[1])
latitudePhi = float(sys.argv[2])
longitudeLambda = float(sys.argv[3])

# convert degrees to radians
radianCenterLambda = math.radians(centerLambda)
radianLatitudePhi = math.radians(latitudePhi)
radianLongitudeLambda = math.radians(longitudeLambda)

# formulas for x and y coordinate projections (need to use radians for sin)
radianX = radianLongitudeLambda - radianCenterLambda
radianY = 0.5 * math.log((1 + math.sin(radianLatitudePhi)) / (1 - math.sin(radianLatitudePhi)))

# convert back to degrees
x = math.degrees(radianX)
y = math.degrees(radianY)

# print out x & y projection
stdio.writeln("Projection in Radians: x=" + str(radianX) + ", y=" + str(radianY))
stdio.writeln("Projection in Degrees: x=" + str(x) + ", y=" + str(y))





