#!/usr/bin/python
import common

TABLES_DIR = "./tables/"

def get_w_over_l( csv_fname , k_prime_in_m , abs_v_t_in_V ) :
	data_matrix = common.read_csv_rows( csv_fname )
	w_over_l_arr = [ ]
	for row in data_matrix :
		i_drain = row[ 1 ]
		v_in = row[ 0 ]
		if isinstance( i_drain , float ) and i_drain != 0.00 :
			# Data point comes from saturation region. Apply formula.
			w_over_l_arr.append( ( 2 * i_drain ) / ( k_prime_in_m * ( ( v_in - abs_v_t_in_V ) ** 2.0 ) ) )
	return float( sum( w_over_l_arr ) ) / len( w_over_l_arr )

if __name__ == "__main__" :
	PREC = 3
	# Threshold voltages
	threshold_voltages = common.read_csv_rows( TABLES_DIR + "vt.csv" )
	nmos_vt = threshold_voltages[ 1 ][ 0 ]
	pmos_vt = threshold_voltages[ 1 ][ 1 ]
	# Process transconductance parameters k
	k_vals = common.read_csv_rows( TABLES_DIR + "k.csv" )
	nmos_k = k_vals[ 1 ][ 0 ]
	pmos_k = k_vals[ 1 ][ 1 ]
	# W over L
	w_over_l_nmos = get_w_over_l( TABLES_DIR + "data_1.csv" , nmos_k , nmos_vt )
	w_over_l_pmos = get_w_over_l( TABLES_DIR + "data_3.csv" , pmos_k , abs( pmos_vt ) )
	data_matrix_w_l = [ [ "W over L - NMOS" , "W over L - PMOS" ] , [ common.set_precision_str( w_over_l_nmos , PREC ) , common.set_precision_str( w_over_l_pmos , PREC ) ] ]
	common.write_csv_from_matrix( TABLES_DIR + "w_over_l.csv" , data_matrix_w_l )
