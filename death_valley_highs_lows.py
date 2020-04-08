# Comma-Separated Values (CSV) Parsing: Error Checking

# Import Python CSV module
import csv

# Import Pythin datetime module
from datetime import datetime

# Imports the Matplotlib library
import matplotlib.pyplot as plt

# Set path of file to 'filename' variable
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        # Try to get the value in each position for the high and low temperatures
        try:
            high = int(row[4])
            low = int(row[5])
        
        # If a ValueError is thrown, then print the error message and continue the loop
        except ValueError:
            print(f'Error: Missing data for {current_date}.')
        
        # If no error, append date, high temperature, and low temperature to their respective lists 
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # Adjust opacity (alpha) of highs plots to 0.5
ax.plot(dates, lows, c='blue', alpha=0.5) # Adjust opacity (alpha) of lows plots to 0.5
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Shades the area between the highs and lows plots with opacity (alpha) of 0.1

# Format plot title, axis labels, and ticks 
plt.title('Daily High and Low Temperatures - 2018\nDeath Valley, California', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()