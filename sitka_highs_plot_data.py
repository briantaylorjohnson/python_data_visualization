# Comma-Separated Values (CSV) Parsing: Extract and Read Data

# Imports the Python CSV module
import csv

# Imports the Matplotlib library
import matplotlib.pyplot as plt

# Specifies the file we want to open
filename = 'data/sitka_weather_07-2018_simple.csv'

# Opens the file with the path in the filename variable
with open(filename) as f:

    """ Uses reader to read and parse the CSV file """
    reader = csv.reader(f)

    # next() function in CSV module reads each line
    # Here we read the first line to get the header row and print it out in the terminal
    header_row = next(reader)
    
    # Get high temperatures from this file
    highs = []

    # Loops through every line in reader dictionary (where each row is a list of values separated by a comma)
    for row in reader:
        high = int(row[5]) # Sets the value in position five of the row to 'high' variable
        highs.append(high) # Appends the 'high' variable value to the highs list

    # Plot the high temps and adds styling
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs, c='red')

    # Format plot title, axis labels, and ticks 
    plt.title('Daily High Temperature - July 2018', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()