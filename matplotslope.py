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

#Fitting function
def func(x, a, b, ):
    return a*np.exp(b*x)
    #return a*x+b


style.use('ggplot')
    #Experimental x and y data points   
x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    #Plot experimental data points
plt.plot(x, y, 'r+', label='experimental-data')
 
 
 
    #Perform the curve-fit
popt, pcov = curve_fit(func, x, y)
print(popt)
 
    #x values for the fitted function   
xFit = np.arange(0.0, 1.20, 0.01)
 
    #Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'g', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
 
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
