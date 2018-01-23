#!/usr/bin/python2

# Roman Parise
import numpy as np

# Only take some of the rows and columns from the csv file. Will crash if you try to
# take in strings.
input_fname="example.csv"
print "Input filename: " + input_fname
print ""
csv_matrix = np.loadtxt( input_fname , delimiter="," , skiprows=1 , usecols=(1,2) )
print "Input CSV matrix: "
print csv_matrix

output_csv_matrix = [ [ ( col ** 2 ) for col in row ] for row in csv_matrix ]
print ""
print "Output CSV matrix: "
print output_csv_matrix

output_fname = "example_out.csv"
np.savetxt( output_fname , output_csv_matrix , fmt='%i' )
print ""
print "Output is in " + output_fname
