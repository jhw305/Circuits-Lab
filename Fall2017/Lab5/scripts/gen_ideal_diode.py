#!/usr/bin/python

# Roman Parise

import matplotlib.pyplot as plt
import numpy as np

I0 = 1e-10
Vthermal = 26e-3
infty = 1e25

Va_shock = np.linspace( 0 , 1.0 , 1000 )
shockley_diode = I0 * ( np.exp( Va_shock / Vthermal ) - 1 )

Va_ideal = np.linspace( 0 , 0.7 , 1000 )
ideal_diode = [ 0 ] * ( len( Va_ideal ) - 1 ) + [ infty ]

plt.xlabel( "$V_{applied}$ [ V ]" )
plt.ylabel( "$I_{diode}$ [ A ]" )

plt.ylim( -1 , 100 )

shock_plt, = plt.plot( Va_shock , shockley_diode , label = "Shockley's Diode Equation" )
ideal_plt, = plt.plot( Va_ideal , ideal_diode , label = "Perfectly Ideal Diode" )
plt.legend( handles = [ shock_plt , ideal_plt ] )
plt.savefig( "../images/ideal_diode.PNG" )
