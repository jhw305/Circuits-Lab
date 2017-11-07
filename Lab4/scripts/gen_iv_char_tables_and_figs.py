#!/usr/bin/python

# Roman Parise

import common
from math import exp

# Constant definitions
csv_ext = ".csv"
tables_dir = "../tables/"
gen_csv = lambda name : tables_dir + name + csv_ext
pn_junction_table = gen_csv( "pn_junction_table" )
zener_table = gen_csv( "zener_table" )
schottky_table = gen_csv( "schottky_table" )
R = 300
headings = [ r"Source Voltage [V]" , r"Voltage over Resistor [mV]" , r"Voltage over Diode [V]" , r"Current [uA]" ]

def gen_diode_data_matrix( source_voltages , diode_voltages ) :

	# Generate tables
	data_rows = [ ]
	for v_count in range( 0 , len( source_voltages ) ) :
		source_voltage = source_voltages[ v_count ]
		diode_voltage = diode_voltages[ v_count ]
		resistor_voltage = source_voltage - diode_voltage
		current = resistor_voltage / R
		data_rows.append( [ source_voltage , resistor_voltage * 1e3 , diode_voltage , current * 1e6 ] )

	# Sort by source voltage
	sorted_data_rows = [ ]
	# Not the best sorting algorithm, but it'll do for small lists :)
	sorted_data_rows = [ data_rows[ 0 ] ]
	for data_rows_count in range( 0 , len( data_rows ) ) :
		for sorted_data_rows_count in range( 0 , len( sorted_data_rows ) ) :
			if data_rows[ data_rows_count ][ 0 ] < sorted_data_rows[ sorted_data_rows_count ][ 0 ] :
				sorted_data_rows.insert( sorted_data_rows_count , data_rows[ data_rows_count ] )
				break
		if data_rows[ data_rows_count ] not in sorted_data_rows :
			sorted_data_rows.append( data_rows[ data_rows_count ] )
	data_rows = sorted_data_rows

	# Add headings at the top
	data_rows.insert( 0 , headings )
	return data_rows

# Data
pn_junction_source_voltages = [ 0 , 0.100, 0.200, 0.300, 0.400, 0.499, 0.599, 0.699, 0.799, 0.899, 0.999, 1.099, 1.199, -0.100, -0.200, -0.300, -0.399, -0.499, -0.599, -0.699, -0.799, -0.899, -0.999, -1.498, -1.998, -2.497, -2.997, -3.995, -16.00, -25.00 ]
pn_junction_diode_voltages = [ 0, 0.101, 0.201, 0.301, 0.399, 0.484, 0.536, 0.566, 0.585, 0.600, 0.611, 0.620, 0.629, -0.101, -0.201, -0.301, -0.400, -0.500, -0.600, -0.700, -0.800, -0.900, -1.000, -1.501, -2.001, -2.501, -3.001, -4.001, -16.00, -24.99 ]

zener_source_voltages = [ 0 , 0.099 , 0.199 , 0.299 , 0.599 , 0.698 , 0.798 , 0.898 , 1.198 , -0.100 , -0.200 , -0.300 , -0.400 , -0.499 , -0.599 , -0.699 , -1.199 , -1.998 , -2.997 , -3.995 , -4.095 , -4.195 , -4.294 , -4.494 , -4.993 , -5.493 , -5.992 ]
zener_diode_voltages = [ 0 , 0.099 , 0.199 , 0.299 , 0.590 , 0.647 , 0.674 , 0.690 , 0.716 , -0.101 , -0.201 , -0.301 , -0.400 , -0.500 , -0.600 , -0.700 , -1.201 , -2.000 , -2.982 , -3.809 , -3.873 , -3.935 , -3.993 , -4.098 , -4.306 , -4.455 , -4.563 ]

schottky_source_voltages = [ 0 , 0.100 , 0.200 , 0.300 , 0.400 , 0.499 , 0.599 , 0.699 , 0.799 , 0.899 , 0.999 , -0.100 , -0.200 , -0.300 , -0.399 , -0.499 , -0.999 , -1.498 , -2.997 , -4.995 , -16.00 , -16.00 , -25.00 , -25.00 ]
schottky_diode_voltages = [ 0 , 0.084 , 0.124 , 0.143 , 0.155 , 0.163 , 0.170 , 0.175 , 0.179 , 0.183 , 0.186 , -0.100 , -0.200 , -0.300 , -0.400 , -0.500 , -1.000 , -1.500 , -3.000 , -5.000 , -15.99 , -16.00 , -24.99 , -24.99 ]

# Generate tables
common.write_csv_from_matrix( pn_junction_table , gen_diode_data_matrix( pn_junction_source_voltages , pn_junction_diode_voltages ) )
common.write_csv_from_matrix( zener_table , gen_diode_data_matrix( zener_source_voltages , zener_diode_voltages ) )
common.write_csv_from_matrix( schottky_table , gen_diode_data_matrix( zener_source_voltages , zener_diode_voltages ) )

# Generate figures
# TODO

import matplotlib.pylab as plt

images_dir = "../images/"
pn_fname = "pn_junction_diode"
schottky_fname = "schottky_diode"
zener_fname = "zener_diode"
png_ext = ".PNG"

# generate plot

plt.plot(pn_junction_source_voltages, pn_junction_diode_voltages, 'k')
plt.savefig(images_dir + pn_fname + png_ext)
