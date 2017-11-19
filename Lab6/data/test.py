#!/usr/bin/python

from common import *
import matplotlib.pyplot as plt

TABLES_DIR = "../tables/"
IMAGES_DIR = "../images/"
CSV_EXT = ".csv"
PNG_EXT = ".PNG"

PREC = 3
R1 = 0.998e3
R2 = 9.902e3

# MOSFET Circuit 1
mosfet_circuit_1_fname = "mosfet_id_vgs"
mosfet_circuit_1_data_fname = TABLES_DIR + mosfet_circuit_1_fname + CSV_EXT
mosfet_circuit_1_fig_fname = IMAGES_DIR + mosfet_circuit_1_fname + PNG_EXT
V2 = 10
V1 = [ 0 , 0.5 , 1 , 1.5 , 2 , 2.05 , 2.10 , 2.15 , 2.20 , 2.25 , 2.30 , 2.35 , 2.40 , 2.45 , 2.5 , 3 , 3.5 , 4 , 4.5 , 5 ] # 0 - 5V
Vr2 = [ 0 , 0 , 0 , 0 , 0.064 , 0.127 , 0.225 , 0.418 , 0.702 , 1.211 , 1.885 , 3.025, 4.314 , 6.309 , 8.172 , 9.965 , 9.978 , 9.983 , 9.985 , 9.987 ]
I_D = [ 1e3 * ( data_point / R2 ) for data_point in Vr2 ]
Vgs = [ 0 , 0.500 , 0.999 , 1.500 , 1.999 , 2.05 , 2.100 , 2.150 , 2.20 , 2.25 , 2.30 , 2.35 , 2.40 , 2.45 , 2.498 , 2.998 , 3.497 , 3.996 , 4.497 , 4.996 ]

plt.plot( Vgs , I_D )
plt.xlabel( "$V_{GS}$ [ V ]" )
plt.ylabel( "$I_D$ [ mA ]" )
plt.savefig( mosfet_circuit_1_fig_fname )

data_matrix_mosfet_1 = []
for row_count in range( 0 , len(  V1 ) ) :
	row = [ V1[ row_count ] , Vr2[ row_count ] , I_D[ row_count ] , Vgs[ row_count ] ]
	data_matrix_mosfet_1.append( [ set_precision_str( data_point , PREC ) for data_point in row ] )
data_matrix_mosfet_1_headings = [ "$V_1$ [ V ]" , "$V_{R2}$ [ V ]" , "$I_D$ [ mA ]" , "$V_{GS}$ [ V ]" ]
data_matrix_mosfet_1 = [ data_matrix_mosfet_1_headings ] + data_matrix_mosfet_1
write_csv_from_matrix( mosfet_circuit_1_data_fname , data_matrix_mosfet_1 )
