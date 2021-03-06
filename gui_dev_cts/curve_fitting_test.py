
import warnings
import tkinter as tk
from tkinter.ttk import *
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
from scipy.misc import derivative
import fileinput
coord = []
def plotg():

    
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')
        
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        p20 = np.poly1d(np.polyfit(x, y, 20))

    print(p20(69))

    xp=np.linspace(0.2,1.4,180)
    ax.plot(x, y, '.',label='experimetal data')
    ax.plot( xp, p20(xp), 'r', label='fitted data')
    # Defining the cursor
    cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = 'b', linewidth = .5)
# Creating an annotating box
    annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox=dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
    annot.set_visible(False)
# Function for storing and showing the clicked values
    
    def onclick(event):
        global coord
        coord.append((event.xdata, event.ydata))
        x = event.xdata
        y = event.ydata
        print([x,y])
        annot.xy = (x,y)
        text = "({:.2g},{:.2g})".format( x,y )
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw() #redraw the figure
    fig.canvas.mpl_connect('button_press_event', onclick)
    
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()
    plt.show()


plotg()