#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

first_half = np.linspace( 0 , 0.7 , 100 )
second_half = np.linspace( 0.701 , 1.5 , 100 )

first_half__id = [ 0 ] * len( first_half )
second_half__id = np.exp( 3*(second_half - 0.701) ) - 1

v_gs = np.concatenate( [ first_half , second_half ] )
_id = np.concatenate( [ first_half__id , second_half__id ] )

plt.xlabel( "$V_{GS}$" )
plt.ylabel( "$I_{D}$" )
plt.plot( v_gs , _id )
plt.savefig( "../images/id_vs_vgs.PNG" )
