#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

Vf = 2
ts = 4

region1 = np.linspace( -10 , 0 , 100 )
region2 = np.linspace( 0.01 , ts , 100 )

region1_v = np.array( [ Vf ] * len( region1 ) )
region2_v = Vf * np.sqrt( 1 - ( ( region2 / ts ) ** 2 ) )

t = np.concatenate( [ region1 , region2 ] )
v = np.concatenate( [ region1_v , region2_v ] )

plt.plot( t , v )
plt.ylim( 0 , 4 )
plt.xlabel( "t" )
plt.ylabel( "$V_{diode}$" )
plt.savefig( "diode_voltage.PNG" )
