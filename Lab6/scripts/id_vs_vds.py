#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

first_half_1 = np.linspace( 0 , 0.7 , 100 )
second_half_1 = np.linspace( 0.701 , 1.5 , 100 )
first_half_1_id = first_half_1
second_half_1_id = [ 0.701 ] * len( second_half_1 )

first_half_2 = np.linspace( 0 , 0.9 , 100 )
second_half_2 = np.linspace( 0.901 , 1.5 , 100 )
first_half_2_id = first_half_2
second_half_2_id = [ 0.901 ] * len( second_half_2 )

first_half_3 = np.linspace( 0 , 1.1 , 100 )
second_half_3 = np.linspace( 1.101 , 1.5 , 100 )
first_half_3_id = first_half_3
second_half_3_id = [ 1.101 ] * len( second_half_3 )

v_gs_1 = np.concatenate( [ first_half_1 , second_half_1 ] )
id_1 = np.concatenate( [ first_half_1_id , second_half_1_id ] )

v_gs_2 = np.concatenate( [ first_half_2 , second_half_2 ] )
id_2 = np.concatenate( [ first_half_2_id , second_half_2_id ] )

v_gs_3 = np.concatenate( [ first_half_3 , second_half_3 ] )
id_3 = np.concatenate( [ first_half_3_id , second_half_3_id ] )

plt.plot( v_gs_1 , id_1 )
plt.plot( v_gs_2 , id_2 )
plt.plot( v_gs_3 , id_3 )

plt.xlabel( "$V_{DS}$" )
plt.ylabel( "$I_{D}$" )
plt.savefig( "../images/id_vs_vds.PNG" )
