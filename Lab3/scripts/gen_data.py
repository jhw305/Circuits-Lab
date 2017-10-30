#!/usr/bin/env python

# gen_data.py
# Generate tables for Lab 3 four-point probe
from math import log
from math import pi
import sys

# Exit codes
SUCCESS = 0
FAILURE = 1

try:
	import common
except ImportError:
	print( "Cannot import common library." )
	print( "Please go to the repo's root directory/common/scripts/ and run \"sudo python setup.py install\"." )
	sys.exit( FAILURE )

TABLES_DIR = "../tables/"

# Data table - four point probe
DATA_TABLE_FNAME = "data_table_4ptprobe.csv"
voltage = 2.3e-3
current = 56.5e-6
s = 1.25e-3
d = 2e-2
t = 280e-6

data_headings = [ r"Voltage [mV]" , r"Current [uA]" , r"s [mm]" , r"d [cm]" , r"t [um]" ]
data_row = [ voltage * 1e3 , current * 1e6 , s * 1e3 , d * 1e2 , t * 1e6 ]
common.write_csv_from_matrix( TABLES_DIR + DATA_TABLE_FNAME , [ data_headings , data_row ] )

# Results table - four point probe
RESULTS_TABLE_FNAME = "results_table_4ptprobe.csv"
correction_factor = pi / log( 2 )
sheet_res = ( correction_factor * voltage ) / current
rho = sheet_res * t

results_headings = [ r"Sheet Resistance [Ohm]" , r"Resistivity [Ohm-mm]" ]
results_row = [ common.set_precision_str( sheet_res ) , common.set_precision_str( rho * 1e3 ) ]
common.write_csv_from_matrix( TABLES_DIR + RESULTS_TABLE_FNAME , [ results_headings , results_row ] )

sys.exit( SUCCESS )
