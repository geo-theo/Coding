### 2.1.13 ###
######################################################################################################################################################
### Given two stars with angles of declination and right ascension (d1, a1) and (d2, a2), the angle they subtend is given by the Haversine formula ###
### Compose a program to take declination and right ascension of two stars as command-line arguments and write the angle they subtend. ###############
######################################################################################################################################################
import stdio
import sys
import math

def starAngle(d1, a1, d2, a2):
    # convert degrees to radians
    d1 = math.radians(d1)
    a1 = math.radians(a1)
    d2 = math.radians(d2)
    a2 = math.radians(a2)

    # compute differences to get a and d according to formula
    a = a2 - a1
    d = d2 - d1

    # harversine formula
    angle_rad = 2 * math.asin(((math.sin(d/2))**2 + math.cos(d1) * math.cos(d2) * (math.sin(a/2))**2)**0.5)
    # simplified haversine formula
    ## angle_rad = 2 * math.asin(math.sqrt(math.sin(d / 2)**2 + math.cos(d1) * math.cos(d2) * (math.sin(a / 2)**2)))

    # convert from radians back to degrees
    angle_deg = math.degrees(angle_rad)

    # output angle result in both radians and degrees
    return angle_rad, angle_deg

# take inputs as angles of declination and right ascension
d1 = float(sys.argv[1])
a1 = float(sys.argv[2])
d2 = float(sys.argv[3])
a2 = float(sys.argv[4])

# execute function on inputs
angle_rad, angle_deg = starAngle(d1, a1, d2, a2)

# print results in both radians and degrees
stdio.writeln("Angle subtended between stars:" + str(angle_rad) + " radians; " + str(angle_deg) + " degrees.")