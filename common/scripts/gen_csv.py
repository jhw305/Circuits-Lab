#Jason Wang

import sys
import argparse
import csv
import numpy as np

#parser = argparse.ArgumentParser()
#parser.add_argument('-f', dest='fname', help='Set file name')
#parser.add_argument('-l', type=int, dest='num_elements', help='Set number of elements (length of row)')
#parser.add_argument('-h', dest='h_list', help='Set row header name')
#parser.add_argument('-n', nargs='3', type=int, dest='n_list', help='Set min, max, and step for list')


arguments = len(sys.argv) - 1


with open(sys.argv[1]) as csvfile:
	writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)

	num_elements = int(sys.argv[2])	
	position = 3

	while (arguments >= position):
		min_value = int(sys.argv[position + 1])
		max_value = int(sys.argv[position + 2])
		if min_value != 0 and max_value != 0:
			writer.writerow(sys.argv[position] + np.linspace(min_value, max_value, num_elements))
		else:
			writer.writerow(sys.argv[position] + [' '] * num_elements)
		position += 3		
