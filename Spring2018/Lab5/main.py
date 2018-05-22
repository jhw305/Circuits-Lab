#!/usr/bin/python
import common
import math

def latex_const( const_name , const_val ) :
	return "\\newcommand{\\" + str( const_name ) + "}{" + str( const_val ) + "}"

def parallel( x , y ) :
	return ( x * y ) / ( x + y )

PREC = 2
TABLES_DIR = "./tables/"

I_SS = 450e-6 # Amperes
V_DD = 5.0 # Volts

W = 200e-6 # Meters
L = 10e-6 # Meters

kn_prime = 0.6e-3 # A/V
kn = kn_prime * ( W / L ) # A/V
kp_prime = 0.6e-3 # A/V
kp = kp_prime * ( W / L ) # A/V

lambda_n = 0.005 # V^-1
lambda_p = 0.01 # V^-1

Vtn = 1.4 # Volts
Vtp = -1.0 # Volts

V_bias = 2.5 # Volts

if __name__ == "__main__" :

	# Calculate resistors
	vgs_current_src = Vtn + math.sqrt( I_SS / kn )
	r_ref = ( 2 * ( V_DD  - vgs_current_src ) / I_SS )
	V_midpoint = ( V_DD + ( V_bias - Vtn ) ) / 2.0
	r_d = ( 2 * ( V_DD - V_midpoint ) ) / I_SS

	# Generate constants file
	
	# FET and amp spec
	const_text = latex_const( "iss" , str( I_SS * 1e6 ) + "\\si{\\micro\\ampere}" ) + common.NEWLINE
	const_text += latex_const( "vdd" , str( V_DD ) + "\\si{\\volt}" ) + common.NEWLINE
	const_text += latex_const( "vmidpoint" , str( V_midpoint ) + "\\si{\\volt}" ) + common.NEWLINE
	const_text += latex_const( "vtn" , str( Vtn ) + "\\si{\\volt}" ) + common.NEWLINE
	const_text += latex_const( "vgsminusvtn" , common.set_precision_str( vgs_current_src - Vtn , PREC ) + "\\si{\\volt}" ) + common.NEWLINE
	const_text += latex_const( "vtp" , str( Vtp ) + "\\si{\\volt}" ) + common.NEWLINE
	const_text += latex_const( "width" , str( W * 1e6 ) + "\\si{\\micro\\meter}" ) + common.NEWLINE
	const_text += latex_const( "length" , str( L * 1e6 ) + "\\si{\\micro\\meter}" ) + common.NEWLINE
	const_text += latex_const( "woverl" , str( W / L ) ) + common.NEWLINE
	const_text += latex_const( "knprime" , str( kn_prime * 1e3 ) + "$\\frac{mA}{V}$" ) + common.NEWLINE
	const_text += latex_const( "kn" , str( kn * 1e3 ) + "$\\frac{mA}{V}$" ) + common.NEWLINE
	const_text += latex_const( "kpprime" , str( kp_prime * 1e3 ) + "$\\frac{mA}{V}$" ) + common.NEWLINE
	const_text += latex_const( "kp" , str( kp * 1e3 ) + "$\\frac{mA}{V}$" ) + common.NEWLINE
	const_text += latex_const( "vbias" , str( V_bias ) + "\\si{\\volt}" ) + common.NEWLINE

	# Calculated resistor values
	const_text += latex_const( "rref" , common.set_precision_str( r_ref * 1e-3 , PREC ) + "\\si{\\kilo\\ohm}" ) + common.NEWLINE
	const_text += latex_const( "rd" , common.set_precision_str( r_d * 1e-3 , PREC ) + "\\si{\\kilo\\ohm}" ) + common.NEWLINE

	with open( "constants.tex" , "w" ) as f :
		f.write( const_text )

	# Gain tables for simulation 1

	id1AB = 225e-6 # Amps	
	VgsAB = 1.593 # Volts
	gm1AB = ( 2.0 * id1AB ) / ( VgsAB - Vtn ) # A / V
	ro1AB = 1.0 / ( lambda_n * id1AB )

	id2AB = 225e-6 # Amps
	ro2AB = 1.0 / ( lambda_n * id2AB ) # A / V
	
	A_dm = 1.0 * gm1AB * parallel( r_d , ro1AB )
	# A_cm = ( -1.0 * gm1AB * r_d ) / ( 1.0 + ( ro2AB * ( gm1AB + ( 1.0 / ro1AB ) ) ) )
	A_cm = - ( gm1AB * r_d * ro1AB ) / ( r_d + ( gm1AB * ( ro1AB ** 2.0 ) ) )

	common.write_csv_from_matrix( TABLES_DIR + "sim1_gain.csv" , [ [ "Differential Mode Gain [V/V]" , "Common Mode Gain [V/V]" , "Common-Mode Rejection Ratio" ] , [ common.set_precision_str( A_dm , PREC ) , common.set_precision_str( A_cm , PREC ) , common.set_precision_str( abs( A_dm / A_cm ) , PREC ) ] ] )

	# Saturation range for sim 2

	common.write_csv_from_matrix( TABLES_DIR + "sim2_sat.csv" , [ [ "" , "Maximum [V]" , "Minimum [V]" ] , [ "DM Output Voltage" , 3.8794 , -3.8957 ] , [ "DM Input Voltage" , 291.89e-3 , -308.75e-3 ] ] )

	# Gain tables for sim 2

	A_dm_sim2 = 20.03

	common.write_csv_from_matrix( TABLES_DIR + "sim2_gain.csv" , [ [ "Theoretical Calculation [V/V]" , "Simulation Result [V/V]" , "Error" ] , [ common.set_precision_str( A_dm , PREC ) , A_dm_sim2 , common.fmt_perc_err( A_dm_sim2 , A_dm , PREC ) ] ] )

	# Saturation range for sim 3
	

	# Gain tables for sim 3
	A_cm_sim3 = -0.01
	common.write_csv_from_matrix( TABLES_DIR + "sim3_gain.csv" , [ [ "Theoretical Calculation [V/V]" , "Simulation Result [V/V]" , "Error" ] , [ common.set_precision_str( A_cm , PREC ) , A_cm_sim3 , common.fmt_perc_err( A_cm_sim3 , A_cm , PREC ) ] ] )
