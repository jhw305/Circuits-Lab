#!/usr/bin/python

# Roman Parise
# Common functions for data processing
WRITE="w"
COMMA_DELIMITER=","
NEWLINE="\n"
CSV_EXT=".csv"

def perc_err( measured , theoretical ):
	return abs( ( measured - theoretical ) / theoretical )

def fmt_perc_err( measured , theoretical ) :
	return fmt_perc( perc_err( measured , theoretical ) )

# TODO: Make the precision on these variable
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
