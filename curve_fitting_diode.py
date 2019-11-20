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
from matplotlib.widgets import Cursor
import mplcursors
def func(x, a, b):
    return a*np.exp(b*x)

quadratic = lambda x,p: p[0]*(x**2)+p[1]*x+p[2]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#CFFBFF')


x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    #Plot experimental data points
cursor = Cursor(ax, useblit=False, color='black', linewidth=0.5)
ax.plot(x, y, 'r+', label='experimental-data')
fitcoeffs=polyfit(x,y,2)
print(fitcoeffs)


xFit = np.arange(0.0, 1.20, 0.01)
popt, pcov = curve_fit(func, x, y)
print(popt)
 

 
#Plot the fitted function
ax.plot(xFit, func(xFit, *popt), 'g', label='fit params(ae^bx): a=%5.3f, b=%5.3f' % tuple(popt)) 
#Plot the fitted function
#ax.plot(x, quadratic(x, fitcoeffs), 'b.', label='fit params(ax^2+bx+c) : a=%5.3f, b=%5.3f,c=%5.3f' % tuple(fitcoeffs))
mplcursors.cursor(multiple=True).connect(
    "add", lambda sel: sel.annotation.draggable(False))
#plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
plt.xlabel('Vd(volts)')
plt.ylabel('Id(amperes)')
plt.legend()
plt.show()
