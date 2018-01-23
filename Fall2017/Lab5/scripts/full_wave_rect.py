#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

V0 = 10
Vth = 0.7

t = np.linspace( 0 , 100 , 10000 )
Vin = V0 * np.sin( 0.2 * t )
Vout = np.array([])
for point in Vin:
	out_val = 0
	if abs( point ) > 2 * Vth:
		out_val = abs( point ) - ( 2 * Vth )
	Vout = np.append( Vout , [ [ out_val ] ] )
vin_plt, = plt.plot( t , Vin , label = "$V_{in}$" )
vout_plt, = plt.plot( t , Vout , label = "$V_{out}$" )
plt.tick_params( labelbottom = 'off' )
plt.xlabel( "t" )
plt.ylabel( "$V_{A}$" )
plt.legend( handles = [ vin_plt , vout_plt ] )
plt.savefig( "../images/full_wave_rect.PNG" )
