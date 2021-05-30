import serial
import time
import math
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
import warnings
phrase='DONE'
'''def convert():
    for line in fileinput.input('points.txt', inplace=True):
        if phrase in line:
            continue
        print(line, end='')
    csv_data=open('points.txt','r')
    lines=csv_data.readlines()
    csv_data.close()
    #print(lines)
    lines=[line.strip() for line in lines]
    #print(lines)
    csv_op=open('datapoints.txt','w')
    csv_op.close()

    
    res = []
    [res.append(x) for x in lines if x not in res]
    

        # printing list after removal 
    #print ("The list after removing duplicates : " + str(res))
    
    for line in res:
        data_sep=line.split(',')
        vdadc=int(data_sep[0])
        idadc=int(data_sep[1])
        #print(vdadc)
        #print(f" {vdadc} , {idadc} ")
        voltage=round(vdadc*.00654, 3)
        current=np.log(round(((idadc*.00654)/6.67)/4.7, 3))
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")d
        #print(voltage)
        print(current)
        csv_val=','.join([str(voltage),str(current)])
        csv_op=open('datapoints.txt','a')
        #print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()'''
coord = []
def plotg():
    
    e=2.718
    
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')
        
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    x_log,y_log = np.loadtxt('logpoints.txt',
                    unpack=True,
                    delimiter = ',')
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        p20 = np.poly1d(np.polyfit(x, y, 20))

    p = np.polyfit(x_log, y_log, 1)

    print(p)
    xlp=np.linspace(0.08,1.126,180)  #V vs ln(I) curve fitting

    F=(math.exp(p[1]))*(e**(p[0]*xlp))
    ax.plot(x, y, '.',label='experimetal data')
    #ax.plot(x_log, y_log, '+',label='log data')
    xp=np.linspace(0.192,1.126,180)   #V vs I curve fitting
    
    ax.plot(xlp, F, 'g',label='linear fit')
    ax.plot( xp, p20(xp), 'r', label='20th order fit')
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

#convert()
plotg()