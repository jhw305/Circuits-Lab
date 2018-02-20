#Jason Wang

import sys
import csv
import numpy as np

arguments = len(sys.argv) - 1

with open(sys.argv[1] + '.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)

	num_elements = int(sys.argv[2])
	position = 3

	while (arguments >= position):
		min_value = int(sys.argv[position + 1])
		max_value = int(sys.argv[position + 2])
		if min_value != 0 or max_value != 0:
			writer.writerow([sys.argv[position]] + (np.linspace(min_value, max_value, num_elements)).tolist())
		else:
			writer.writerow([sys.argv[position]] + [''] * num_elements)
		position += 3
