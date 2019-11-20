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
from matplotlib.widgets import Cursor, Button
import mplcursors
#Fitting function
def func(x, a, b, ):
    return a*np.exp(b*x)
    #return a*x+b
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#FFFFCC')

style.use('ggplot')
    #Experimental x and y data points   
x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')



# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)


    #Plot experimental data points
ax.plot(x, y, 'r+', label='experimental-data')
 
 
 
    #Perform the curve-fit
popt, pcov = curve_fit(func, x, y)
print(popt)
 
    #x values for the fitted function   
xFit = np.arange(0.0, 1.20, 0.01)
 
    #Plot the fitted function
ax.plot(xFit, func(xFit, *popt), 'g', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
cursor = Cursor(ax, useblit=False, color='blue', linewidth=0.5)
mplcursors.cursor(multiple=True).connect(
    "add", lambda sel: sel.annotation.draggable(False))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
