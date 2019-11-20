import serial
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib import style
from scipy.optimize import curve_fit
import numpy as np
from scipy import polyfit
def func(x, a, b):
    return a*np.exp(b*x)

quadratic = lambda x,p: p[0]*(x**2)+p[1]*x+p[2]




x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    #Plot experimental data points
plt.plot(x, y, 'r+', label='experimental-data')
fitcoeffs=polyfit(x,y,2)
print(fitcoeffs)


xFit = np.arange(0.0, 1.20, 0.01)
popt, pcov = curve_fit(func, x, y)
print(popt)
 

 
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'g^', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt)) 
#Plot the fitted function
plt.plot(x, quadratic(x, fitcoeffs), 'b.', label='fit params: a=%5.3f, b=%5.3f,c=%5.3f' % tuple(fitcoeffs))

plt.xlabel('Vd(volts)')
plt.ylabel('Id(amperes)')
plt.legend()
plt.show()
