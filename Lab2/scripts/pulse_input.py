#!/usr/bin/python

# Roman Parise
# Generate tables for pulse input section

import common

R = 10e3
C = 1e-9
theoretical_t = ( R * C )
t_lpf = [ 8.6e-6 , 17.6e-6/2.0 , 27.0e-6/3.0 , 37.2e-6/4.0 ]
t_hpf = [ 8.8e-6 , 18.2e-6/2.0 , 28.0e-6/3.0 ]
DELIMITER = ","
PRECISION = 1
error_heading = "Percentage Error"
tables_dir = "../tables/"

# R and C values
R_heading = r"Resistance [kOhms]"
C_heading = r"Capacitance [nF]"
rc_mat = [ [ R_heading , C_heading ] , [ R / 1e3 , C / 1e-9 ] ]
rc_fname = tables_dir + "R_and_C.csv"
common.write_csv_from_matrix( rc_fname , rc_mat )

def tau_table( t , fname ):
	print( "Theoretical tau [us] = " + str( theoretical_t ) )
	t_val_vs_err = [ [ common.set_precision_str( sample * 1e6 ) , common.fmt_perc( common.perc_err( sample , theoretical_t ) ) ] for sample in t ]
	measured_t_heading = r'Measured Time Constant [us]'
	t_mat = [ [ measured_t_heading , error_heading ] ] + t_val_vs_err
	t_fname = tables_dir + fname
	common.write_csv_from_matrix( t_fname , t_mat )

# Tau table
tau_table( t_lpf , "tau_lpf.csv" )
tau_table( t_hpf , "tau_hpf.csv" )
