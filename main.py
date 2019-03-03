#!/usr/bin/python3
import csv, sys

if len(sys.argv) != 3:
	sys.exit(1)	# parameter required

with open(sys.argv[1], 'r') as csv_file:
	N = int(sys.argv[2])
	csv_reader = csv.reader(csv_file)

	for idx, row in enumerate(csv_reader):
		if idx == N-1:
			print(row)
	
