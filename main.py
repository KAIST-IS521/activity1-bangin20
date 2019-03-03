#!/usr/bin/python3
import csv, sys
import mimetypes

if len(sys.argv) != 3:
    sys.exit(1)	# parameter required

dialect = 0
header = False

with open(sys.argv[1], 'r') as csv_file:
    N = int(sys.argv[2])
    sniffer = csv.Sniffer()

    s = csv_file.read()
    try:
        # Validate CSV File
        dialect = sniffer.sniff(s)
    except:
        print("Invalid CSV File Format")
        sys.exit(1)
    print(sniffer.has_header(s))

with open(sys.argv[1], 'r') as csv_file:
    csv_reader = csv.reader(csv_file, dialect=dialect)

    for idx, row in enumerate(csv_reader):
        if idx == N-1:
            print(row)
