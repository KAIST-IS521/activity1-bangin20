#!/usr/bin/python3
import csv, sys
import mimetypes

if len(sys.argv) != 3:
    print("USAGE ./main.py [FILE_NAME] [LINE_NUM]")
    sys.exit(1)	# parameter required

dialect = 0
header = False
try:
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

        if dialect.delimiter != ',':
            print('Invalid Delimiter')
            sys.exit(1)

        header = sniffer.has_header(s)
        lines = s.split('\n')
        max_column = len(lines[0].split(','))

        if N == 0 or N > max_column:
            print("Invalid Column Number")
            sys.exit(1)

        target_column = ('\n').join(list(i.split(',')[N-1] for i in lines))
        print(target_column)
except:
    print('File Does Not Exist')
    sys.exit(1)
