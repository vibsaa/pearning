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
from tqdm import tqdm_gui
from scipy.misc import derivative

def plotg():
    def func(x, a, b):
        return a*np.exp(b*x)

    quadratic = lambda x,p: p[0]*(x**2)+p[1]*x+p[2]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')
    
    def onpick(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        points = tuple(zip(xdata[ind], ydata[ind]))
        slope=(points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        rd=1/slope
        #print('onpick points:', points)
        print('slope:', slope)
        print('Dynamic resistance:', rd)
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    #Plot experimental data points
    cursor = Cursor(ax, useblit=False, color='black', linewidth=0.5)
    ax.plot(x, y, 'r+', label='experimental-data')
    fitcoeffs=polyfit(x,y,2)
    print(fitcoeffs)


    xFit = np.arange(0.0, 3.3, 0.01) #PUT MAX VALUE OF RANGE =1.2 FOR 1N4007 &=.53 FOR IN5819 &=3.5 for LED
    popt, pcov = curve_fit(func, x, y)
    print(popt)
    #Plot the fitted function 
    ax.plot(xFit, func(xFit, *popt), 'g', label='fit params(ae^bx): a=%5.3f, b=%5.3f' % tuple(popt), picker=5) 
    fig.canvas.mpl_connect('pick_event', onpick)
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    #plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()

plotg()