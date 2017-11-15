#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

If = 3
Ir = 2
t_s = 4

region1 = np.linspace( -10 , 0 , 100 )
region2 = np.linspace( 0.01 , t_s , 100 )
region3 = np.linspace( 4.01 , 10 , 100 )

region1_i = np.array( [ If ] * len( region1 ) )
region2_i = np.array( [ -Ir ] * len( region2 ) )
region3_i = ( -Ir ) * np.exp( -( region3 - t_s ) )

t = np.concatenate( [ region1 , region2 , region3 ] )
i = np.concatenate( [ region1_i , region2_i , region3_i ] )

plt.plot( t , i )
plt.xlabel( "t" )
plt.ylabel( "i(t)" )
plt.savefig( "diode_current.PNG" )
