# Plotting and Styling Individual Points with scatter()

import matplotlib.pyplot as plt

# Data set
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 9, 16, 25]

# Apply style to chart
plt.style.use('seaborn')

# Instantiate fig and ax variables for plotting data
fig, ax = plt.subplots()

# Use scatter() method to plot a single point with x and y coordinates
# s argument sets the size of the dots used to draw the graph
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Render chart
plt.show()
