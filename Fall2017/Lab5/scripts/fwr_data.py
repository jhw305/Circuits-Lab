#!/usr/bin/python

# Roman Parise
# Full-Wave Rectifier Data

# Input src: 20 Vpp

import common

TABLES_DIR = "../tables/"
FWR_DATA_FNAME = "fwr_data.csv"
FWR_ERR_FNAME = "fwr_err.csv"

# Data for peaks and troughs table

rectified_amplitude_peak = 8.906 #V
rectified_amplitude_trough = 8.593 #V

source_peak = 10 #V
source_trough = 10 #V

diff_peak = abs( source_peak - rectified_amplitude_peak )
diff_trough = abs( source_trough - rectified_amplitude_trough )

data_headings = [ "" , "Measured Voltage [ V ]" , "Source Voltage [ V ]" , "Difference [ V ]" ]
peak_data = [ rectified_amplitude_peak , source_peak , diff_peak ]
trough_data = [ rectified_amplitude_trough , source_trough , diff_trough ]
data_matrix = [ data_headings , [ "Peak" ] + peak_data , [ "Trough" ] + trough_data ]

common.write_csv_from_matrix( TABLES_DIR + FWR_DATA_FNAME , data_matrix )

# Errors from theory table

threshold_voltage = 0.7 #V

th_rect_amp = lambda V : abs( V ) - ( 2 * threshold_voltage )
th_rect_amp_peak = th_rect_amp( source_peak )
th_rect_amp_trough = th_rect_amp( source_trough )

data_headings_err = [ "" , "Measured Voltage [ V ]" , "Theoretical Voltage [ V ]" , "Percentage Error" ]
peak_data_err = [ rectified_amplitude_peak , th_rect_amp_peak , common.fmt_perc_err( rectified_amplitude_peak , th_rect_amp_peak ) ]
trough_data_err = [ rectified_amplitude_trough , th_rect_amp_trough , common.fmt_perc_err( rectified_amplitude_trough , th_rect_amp_trough ) ]
data_matrix_err = [ data_headings_err , [ "Peak" ] + peak_data_err , [ "Trough" ] + trough_data_err ]

common.write_csv_from_matrix( TABLES_DIR + FWR_ERR_FNAME , data_matrix_err )
