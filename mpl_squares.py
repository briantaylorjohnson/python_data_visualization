# Initial mpl_squares.py file for data visualization practice

import matplotlib.pyplot as plt

# List of data points
squares = [1, 4, 9, 16, 25]

# fig represents the entire figure or collection of plots
# ax represents a single plot in the figure
fig, ax = plt.subplots()

# Plots the data in squares list
ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Opens Matplotlibs's viewer and displays the plots in squares list
plt.show ()