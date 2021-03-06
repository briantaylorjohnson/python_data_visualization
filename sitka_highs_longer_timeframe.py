# Comma-Separated Values (CSV) Parsing: Visualization with Longer Timeframe 

# Imports the Python CSV module
import csv

# Import Pythin datetime module
from datetime import datetime

# Imports the Matplotlib library
import matplotlib.pyplot as plt

# Specifies the file we want to open
filename = 'data/sitka_weather_2018_simple.csv'

# Opens the file with the path in the filename variable
with open(filename) as f:

    """ Uses reader to read and parse the CSV file """
    reader = csv.reader(f)

    # next() function in CSV module reads each line
    # Here we read the first line to get the header row and print it out in the terminal
    header_row = next(reader)
    
    # Get dates and high temperatures from this file
    dates, highs = [], []

    # Loops through every line in reader dictionary (where each row is a list of values separated by a comma)
    for row in reader:
        # Sets the value in position two of the right to 'current_date' variable
        # This also converts the date string to a datetime object to make it easier to work with
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5]) # Sets the value in position five of the row to 'high' variable
        dates.append(current_date) # Appends the 'current_date' variable value to the dates list
        highs.append(high) # Appends the 'high' variable value to the highs list

    # Plot the high temps and adds styling
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot title, axis labels, and ticks 
    plt.title('Daily High Temperature - 2018', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()