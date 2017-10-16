#!/usr/bin/python2
# Roman Parise
# scope_voltage.py
# Used to calculate the oscilloscope's expected measured voltage and percentage errors

from math import pi

def perc_err( theoretical , experimental ) :
	return abs( 100 * ( theoretical - experimental ) / ( theoretical ) )

def fmt_output( r , f , experimental_ratio ):
	print "-----------------------"
	print "R = " + str( r ) + " , f = " + str( f )
	print "V_scope/V_AC = " + str( v_scope_over_v_src( r , f ) )
	print "Error: " + str( perc_err( v_scope_over_v_src( r , f ) , experimental_ratio ) ) + "%"
	print "-----------------------"

freqs = [ 1e3 , 1e6 ]
res = [ 1e3 , 1e6 ]

r_scope = 1e6
c_scope = 12e-12
z_scope = lambda f : 1 / ( ( 1 / r_scope ) + complex( 0 , 2 * pi * f * c_scope ) )
v_scope_over_v_src = lambda r , f : abs( z_scope( f ) / ( z_scope( f ) + r ) )

fmt_output( res[ 0 ] , freqs[ 0 ] , 10.25/10 )
fmt_output( res[ 0 ] , freqs[ 1 ] , 9.31/10 )
fmt_output( res[ 1 ] , freqs[ 0 ] , 5.00/10 )
fmt_output( res[ 1 ] , freqs[ 1 ] , 0.1/10 )
