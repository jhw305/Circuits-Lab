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
plt.clf( )

data_matrix_mosfet_1 = []
for row_count in range( 0 , len(  V1 ) ) :
	row = [ V1[ row_count ] , Vr2[ row_count ] , I_D[ row_count ] , Vgs[ row_count ] ]
	data_matrix_mosfet_1.append( [ set_precision_str( data_point , PREC ) for data_point in row ] )
data_matrix_mosfet_1_headings = [ "$V_1$ [ V ]" , "$V_{R2}$ [ V ]" , "$I_D$ [ mA ]" , "$V_{GS}$ [ V ]" ]
data_matrix_mosfet_1 = [ data_matrix_mosfet_1_headings ] + data_matrix_mosfet_1
write_csv_from_matrix( mosfet_circuit_1_data_fname , data_matrix_mosfet_1 )

# MOSFET Circuit 2
mosfet_circuit_2_fname = "mosfet_id_vds"
mosfet_circuit_2_data_fname = TABLES_DIR + mosfet_circuit_2_fname + CSV_EXT
mosfet_circuit_2_fig_fname = IMAGES_DIR + mosfet_circuit_2_fname + PNG_EXT
V1_2 = 2.3
V2_2 = [0, 0.1 , 0.2, 0.3, 0.4 , 0.5 , 0.6 , 0.8, 0.9, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 11 ,12, 13, 14, 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 ]
Vr2_2 = [ 0 , 0.1 , 0.197 , 0.294 , 0.389 , 0.485 , 0.579 , 0.768 , 0.860 , 0.954 , 1.636 , 1.717 , 1.755 , 1.789 , 1.824 , 1.861 , 1.901 , 1.953 , 2.004 , 2.051 , 2.107 , 2.164 , 2.226 , 2.294 , 2.364 , 2.441 , 2.528 , 2.615 , 2.707 , 2.811 , 2.915 , 3.018 , 3.139 , 3.270 ]
I_D_2 = [ 1e3 * ( data_point / R2 ) for data_point in Vr2_2 ]
Vds = [0, 0.004 , 0.007 , 0.012 , 0.021 , 0.026 , 0.031 , 0.038 , 0.045 ,0.052, 0.388, 1.300, 2.256, 3.217, 4.177, 5.144, 6.108, 7.055, 8.001, 8.948, 9.884, 10.833, 11.772, 12.704, 13.635, 14.565, 15.470, 16.380, 17.290, 18.191, 19.083, 19.967, 20.842, 21.724]

plt.plot( Vds , I_D_2 )
plt.xlabel( "$V_{DS}$ [ V ]" )
plt.ylabel( "$I_D$ [ mA ]" )
plt.savefig( mosfet_circuit_2_fig_fname )

data_matrix_mosfet_2 = []
for row_count in range( 0 , len(  V2_2 ) ) :
	row = [ V2_2[ row_count ] , Vr2_2[ row_count ] , I_D_2[ row_count ] , Vds[ row_count ] ]
	data_matrix_mosfet_2.append( [ set_precision_str( data_point , PREC ) for data_point in row ] )
data_matrix_mosfet_2_headings = [ "$V_2$ [ V ]" , "$V_{R2}$ [ V ]" , "$I_D$ [ mA ]" , "$V_{DS}$ [ V ]" ]
data_matrix_mosfet_2 = [ data_matrix_mosfet_2_headings ] + data_matrix_mosfet_2
write_csv_from_matrix( mosfet_circuit_2_data_fname , data_matrix_mosfet_2 )
