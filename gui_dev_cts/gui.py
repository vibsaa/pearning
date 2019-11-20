import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.widgets import Cursor
import mplcursors
def func(x, a, b, c):
    y=a * np.exp(b * x) - c
    return y
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#CFFBFf')

x,y = np.loadtxt('points.txt',
                    unpack=True,
                    delimiter = ',')


p0=[.2,.2,-1]

popt, pcov = curve_fit(func, x, y,p0)
print(popt)


ax.plot(x, y, 'r+', label="Original Data")
xFit = np.arange(0.0, 200, 0.01)






# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=False, color='black', linewidth=.5)


 
    #Plot the fitted function
ax.plot(xFit, func(xFit, *popt), 'g', label='fit params: a=%1.2f, b=%1.2f, c=%1.2f' % tuple(popt))
mplcursors.cursor(multiple=True).connect(
    "add", lambda sel: sel.annotation.draggable(False))
plt.legend()
plt.show()