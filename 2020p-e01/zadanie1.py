import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def funkcja(x):
    return (4-x+x**3)/(6+x-4*x**2+x**3)


plt.axhline(y=0.5, color='r', linestyle='--')
plt.axvline(x=-1, color='r', linestyle='--')
plt.axvline(x=2, color='r', linestyle='--')
plt.axvline(x=3, color='r', linestyle='--')

x1 = np.linspace(-3, -1, 1000)
y1 = funkcja(x1)
plt.plot(x1, y1, color='b')

x2 = np.linspace(-1, 2, 1000)
y2 = funkcja(x2)
plt.plot(x2, y2, color='b')

x3 = np.linspace(2, 3, 1000)
y3 = funkcja(x3)
plt.plot(x3, y3, color='b')

x4 = np.linspace(3, 5, 1000)
y4 = funkcja(x4)
plt.plot(x4, y4, color='b')

plt.ylim(-50, 40)
plt.xlim(-3, 5)

plt.annotate('154749', xy=(1, 0), xycoords='axes fraction', horizontalalignment='left', verticalalignment='top')

plt.show()