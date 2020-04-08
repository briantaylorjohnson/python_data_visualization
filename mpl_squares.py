# Initial mpl_squares.py file for data visualization practice

import matplotlib.pyplot as plt

# List of data points for x and y coordinates
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# fig represents the entire figure or collection of plots
# ax represents a single plot in the figure
fig, ax = plt.subplots()

# Plots the data in input_values and squares lists corresponding to x and y coordinates
# linewidth controls the thickness of the plotted line
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24) # Sets the title of the chart
ax.set_xlabel('Value', fontsize=14) # Sets the label for the x axis
ax.set_ylabel('Square of Value', fontsize=14) # Sets the label for the y axis

# Set size of tick labels
# axis argument specifies the axes to which the formatting should be applied
ax.tick_params(axis='both', labelsize=14) 

# Opens Matplotlibs's viewer and displays the plots in squares list
plt.show ()