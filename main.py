#!/usr/bin/python3
import csv, sys

def ValidateCSV(file_content):
    sniffer = csv.Sniffer()
    try:
        # Validate CSV File with comma separator
        dialect = sniffer.sniff(file_content, delimiters=',')
        return dialect
    except:
        raise csv.Error

def GetNthColumn(csv_file, N, dialect):
    csv_rows = csv.reader(csv_file, dialect=dialect)

    target_column = []
    for i, row in enumerate(csv_rows):
        if i == 0:
            max_column = len(row)
            if N == 0 or N > max_column:
                raise ValueError
        target_column.append(row[N-1])

    result = '\n'.join(target_column) # parse list with enter separator
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("USAGE ./main.py [FILE_NAME] [LINE_NUM]")
        sys.exit(1)	# parameter required

    file_name = sys.argv[1]

    try:
        N = int(sys.argv[2])
        with open(file_name, 'r') as csv_file:
            file_content = csv_file.read()
            try:
                dialect = ValidateCSV(file_content)
                csv_file.seek(0)
                result = GetNthColumn(csv_file, N, dialect)

                print(result)
            except csv.Error:
                print("Invalid CSV Format")
                sys.exit(1)
            except ValueError:
                print('Invalid N range')
                sys.exit(1)
    except FileNotFoundError:
        print('File Does Not Exist')
        sys.exit(1)
    except ValueError:
        print("Column number should be a Integer")
        sys.exit(1)
