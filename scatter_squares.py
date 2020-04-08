# Plotting and Styling Individual Points with scatter()

import matplotlib.pyplot as plt

# Apply style to chart
plt.style.use('seaborn')

# Instantiate fig and ax variables for plotting data
fig, ax = plt.subplots()

# Use scatter() method to plot a single point with x and y coordinates
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Render chart
plt.show()
