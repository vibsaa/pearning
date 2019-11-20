import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


 
#Fitting function
def func(x, a, b):
    return a*np.exp(b*x)
    #return a*x+b
 
#Experimental x and y data points    


style.use('ggplot')

x,y = np.loadtxt('datapoints.txt',
                 unpack=True,
                 delimiter = ',')
 
#Plot experimental data points
plt.plot(x, y, 'r+', label='experimental-data')
 
# Initial guess for the parameters
#initialGuess = [1.0,1.0]    
 
#Perform the curve-fit
popt, pcov = curve_fit(func, x, y)
print(popt)
 
#x values for the fitted function
xFit = np.arange(0.0, 1.130, 0.01)
 
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
 
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()