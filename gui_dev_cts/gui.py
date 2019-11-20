import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    y=a * np.exp(b * x) - c
    return y
x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')


p0=[.2,.2,-1]

popt, pcov = curve_fit(func, x, y,p0)
print(popt)

plt.figure()
plt.plot(x, y, 'r+', label="Original Data")
xFit = np.arange(0.0, 200, 0.01)
 
    #Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'g', label='fit params: a=%1.2f, b=%1.2f, c=%1.2f' % tuple(popt))

plt.legend()
plt.show()