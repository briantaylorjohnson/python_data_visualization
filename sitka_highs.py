# Comma-Separated Values (CSV) Parsing

# Imports the Python CSV module
import csv

# Specifies the file we want to open
filename = 'data/sitka_weather_07-2018_simple.csv'

# Opens the file with the path in the filename variable
with open(filename) as f:

    """ Uses reader to read and parse the CSV file """
    reader = csv.reader(f)

    # next() function in CSV module reads each line
    # Here we read the first line to get the header row and print it out in the terminal
    header_row = next(reader)
    
    # enumerate() function returns the index and value of each item in the header_row list 
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    