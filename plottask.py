# program which displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
# it also displays a plot of the function h(x)=x3 in the range 0 to 10
# these should be mapped on the same plot

# Author: Myles Henehan

import numpy as np
import matplotlib.pyplot as plt

mean = 5
standarddev = 2

histvalues = np.random.randn(1000)

adjustedvalues = histvalues * standarddev + mean

plt.hist(adjustedvalues, label="1000 random values", color="blue")

xvalues = list(range(11))
yvalues = []

def h():
    for num in range(0, 11):
        yvalues.append(num ** 3)

h()
xvalues = list(range(0, 11))

plt.plot(xvalues, yvalues, label="Plot of function h(x) = x3", color="red")

plt.legend()
plt.show()


# Note to self: Work on Labels
