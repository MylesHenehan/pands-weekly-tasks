# Weekly Task 8
# Author: Myles Henehan
# Instructions: Program should display a histogram of a normal distribution of 1000 values, with a mean of 5 and standard deviation of 2.
# It should also display a plot of the function h(x)=x^3 in the range 0 to 10. These should be mapped on the same plot.

import numpy as np
import matplotlib.pyplot as plt
# First, we import the libraries that we tend to use for plotting.

mean = 5
standarddev = 2
# Now we assign variables for the standard deviation and the mean.

histvalues = np.random.normal(mean, standarddev, 1000)
# To get 1000 values, we use NumPy's random.normal function, which allows us to customise the standard deviation and the mean.


plt.hist(histvalues, label="1000 random values", color="lightblue")
# Now we plot a histogram with these 1000 values shown in blue.

# Next, we want to plot the function h(x)=x3:

xvalues = list(range(11))
# This uses the range() function to generate integer values from 1 to 10, and converts it to a list.
yvalues = []
# This initiates an empty list where outputs will be stored.

def h():
    for num in range(0, 11):
        yvalues.append(num ** 3)
# Now we're defining a function which iterates over the x values and cubes each one before adding it to the list of y values.

h()
# We now call this function.

plt.plot(xvalues, yvalues, label="Plot of function h(x) = x^3", color="red")
# Now we can plot this function on the same figure.

plt.legend()
# We add a legend to the figure to show which data set is which.

plt.title("Function h(x) = x^3, crossing over a histogram of 1000 random values")
# Let's also add a title for clarity's sake.

plt.show()
# Then we generate the figure.
