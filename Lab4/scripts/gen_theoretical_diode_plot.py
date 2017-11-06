#!/usr/bin/python

# Roman Parise
# Approximate plots of diode's theoretical IV-characteristic

import numpy as np
import matplotlib.pylab as plt

# Constants
i0 = 1e-9
kB = 8.617e-5
T = 300
V_thermal = ( kB * T ) # q is not necessary. It cancels with the "e" in "eV".

images_dir = "../images/"
plt_fname = "ideal_pn_diode"
png_ext = ".PNG"

# Generate plot values
V_gt_100 = np.linspace( -0.1 , 1.25 , 1000 )
V_lt_100 = np.linspace( -105 , -100 , 1000 )

ideal_diode = i0 * ( np.exp( V_gt_100 / V_thermal ) - 1 )
breakdown_approx = -1 * np.exp( - 5 * ( V_lt_100 + 100 ) )

# Generate and save the figure
throwaway_var , ( axes_left , axes_right ) = plt.subplots( 1 , 2 , sharey = True )
axes_left.plot( V_lt_100 , breakdown_approx , clip_on = False )
axes_right.plot( V_gt_100 , ideal_diode , clip_on = False )

axes_left.spines[ 'right' ].set_visible( False )
axes_left.yaxis.tick_left()
axes_right.spines[ 'left' ].set_visible( False )
axes_right.yaxis.tick_right()

axes_left.annotate( 'Breakdown voltage' , xy = ( -104.5 , 0 ) , xytext = ( -103.5 , 0.25e12 ) , arrowprops = dict( facecolor = 'black' , shrink = 0.05 ) )
axes_right.annotate( 'Threshold voltage' , xy = ( 1.125 , 0.5 ) , xytext = ( 0.2 , 0.25e12 ) , arrowprops = dict( facecolor = 'black' , shrink = 0.05 ) )
axes_left.set_ylabel( "Current through the Diode" )
axes_left.set_xlabel( "Voltage over the Diode" )
axes_left.set_yticklabels([])
axes_right.set_yticklabels([])
plt.subplots_adjust( wspace = 0 )
plt.savefig( images_dir + plt_fname + png_ext )
