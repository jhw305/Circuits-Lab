#!/usr/bin/python2

import matplotlib.pyplot as plt
import numpy as np

# For silicon
alpha = 4.73e-4
beta = 636
eg_at_abs_zero = 1.170
T = np.linspace( 0 , 600 , 10000 )
eg = eg_at_abs_zero - ( ( alpha * ( T ** 2 ) ) / ( beta + T ) )

my_fig = plt.figure()

plt.plot( T , eg )
plt.title( "Bandgap Energy versus Temperature" )
plt.xlabel( "Temperature [K]" )
plt.ylabel( "Bandgap Energy [eV]" )
plt.savefig( 'bandgap_graph_plot.pdf' )
