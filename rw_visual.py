# Using Random Walks: Visualization Using RandomWalk() class

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points on the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

# Show plot of random walk
plt.show()

