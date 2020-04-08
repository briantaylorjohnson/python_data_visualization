# Using Random Walks: Styling the Walk

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk
    # Adding the argument increases the points to 50,000 from the default of 5,000
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points on the walk
    # figsize argument is used to adjust the size of the figure
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))

    # Coloring the points as a gradient for each point using a colormap
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Show plot of random walk
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
