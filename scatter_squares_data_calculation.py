# Plotting and Styling Individual Points with scatter()

import matplotlib.pyplot as plt

# Data set
# Sets the x values to all integers from 1 to 1000 inclusive (remember first argument in range() is included in range; second argument is not included in range)
# Sets the y values by calculating the squares of each item in the x_values list using a for loop
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Apply style to chart
plt.style.use('seaborn')

# Instantiate fig and ax variables for plotting data
fig, ax = plt.subplots()

# Use scatter() method to plot a single point with x and y coordinates
# s argument sets the size of the dots used to draw the graph
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Render chart
plt.show()
