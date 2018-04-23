#!/usr/bin/python
import common

def lambda_at_2_5V( ID_1 , ID_2 , VDS_1 , VDS_2 ) :
	return ( ID_2 - ID_1 ) / ( ( ID_1 * VDS_2 ) - ( ID_2 * VDS_1 ) )

if __name__ == "__main__" :

	# NMOS
	nmos_id_1 = 365.191e-6
	VDS_1 = 1.2
	nmos_id_2 = 369.466e-6
	VDS_2 = 3.5
	nmos_lambda = lambda_at_2_5V( nmos_id_1 , nmos_id_2 , VDS_1 , VDS_2 )
	nmos_true_lambda = 0.005

	# PMOS
	pmos_id_1 = 685.976e-6
	VDS_1_pmos = 1.6
	pmos_id_2 = 699.482e-6
	VDS_2_pmos = 3.5
	pmos_lambda = lambda_at_2_5V( pmos_id_1 , pmos_id_2 , VDS_1_pmos , VDS_2_pmos )
	pmos_true_lambda = 0.010

	# Format and write to file
	PREC = 5
	table_headers = [ "" , "Calculated Lambda" , "Model-Specified Lambda" , "Percentage Error" ]
	nmos = [ "NMOS" , common.set_precision_str( nmos_lambda , PREC ) , common.set_precision_str( nmos_true_lambda , PREC ) , common.fmt_perc_err( nmos_lambda , nmos_true_lambda , PREC ) ]
	pmos = [ "PMOS" , common.set_precision_str( pmos_lambda , PREC ) , common.set_precision_str( pmos_true_lambda , PREC ) , common.fmt_perc_err( pmos_lambda , pmos_true_lambda , PREC ) ]
	common.write_csv_from_matrix( "tables/lambda.csv" , [ table_headers, nmos , pmos ] )
