# Plotting and Styling Individual Points with scatter()

import matplotlib.pyplot as plt

# Apply style to chart
plt.style.use('seaborn')

# Instantiate fig and ax variables for plotting data
fig, ax = plt.subplots()

# Use scatter() method to plot a single point with x and y coordinates
ax.scatter(2, 4)

# Render chart
plt.show()
