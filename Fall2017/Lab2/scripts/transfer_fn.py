#!/usr/bin/python2

from math import pi

R = 10e3
C = 1e-9
f = 1 / ( 2 * pi * R * C )

print "Corner frequency: " + str( f )
