#!/usr/bin/python

# Roman Parise
# Common functions for data processing
import csv
import matplotlib.pyplot as plt

WRITE="w"
COMMA_DELIMITER=","
NEWLINE="\n"
CSV_EXT=".csv"

def perc_err( measured , theoretical ):
	return abs( ( measured - theoretical ) / theoretical )

def fmt_perc_err( measured , theoretical ) :
	return fmt_perc( perc_err( measured , theoretical ) )

def set_precision_str( fp_number , prec ):
	return ( ( "%." + str( prec ) + "f" ) % fp_number )

def fmt_perc( perc_as_decimal ):
	return ( set_precision_str( 100 * perc_as_decimal ) ) + "\%"

# TODO: Overwrites files. Is this the best way to do it?
# TODO: Error checking?
def write_csv_from_matrix( fname , matrix ):
	with open( fname , WRITE ) as file_handle:
		for row in matrix:
			str_to_write = COMMA_DELIMITER.join( [ str( element ) for element in row ] )
			file_handle.write( str_to_write + NEWLINE )

# TODO: Needs error checking
# Reads out a csv file into rows
def read_csv_rows( csv_fname ) :
	with open( csv_fname , "rb" ) as csv_file :
		reader = csv.reader( csv_file , delimiter = COMMA_DELIMITER )
		return [ [ float( element ) for element in row ] for row in reader ]

def save_plot_xy( fname , x_list , y_list ) :
	plt.plot( x_list , y_list )
	plt.savefig( fname )
	plt.clf( )

if __name__ == "__main__" :
	rows = read_csv_rows( "test.csv" )
	print( rows )
	save_plot_xy( "test_file.png" , rows[ 0 ] , rows[ 1 ] )
