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
def start():
    ser=serial.Serial(COM.get(), baudrate=115200, timeout=1)
    data1=open('points.txt','w')
    avrdata=0
    progress['value']=0
    root.update_idletasks()
    ser.write(b'D')

    while (avrdata !='DONE'):
        if(ser.in_waiting>0):
            avrdata=ser.readline().decode('ascii')
            data1.write(avrdata)

    progress['value']=100
    root.update_idletasks()    
    ser.close()
    data1.close()
    #popup("Reading process is finished, please proceed!")
    
    
    

def popup(message1):
    window= Tk()
    messagebox.showinfo('System Message', f'{message1}')

    window.deiconify()
    window.destroy()

def convert():
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
    csv_log=open('logpoints.txt','w')
    csv_log.close()

    
    res = []
    [res.append(x) for x in lines if x not in res]
  
        # printing list after removal 
    #print ("The list after removing duplicates : " + str(res))
    for line in res:
        data_sep=line.split(',')
        vdadc=int(data_sep[0])
        idadc=int(data_sep[1])
        #print(f" {vdadc} , {idadc} ")
        voltage=round((vdadc*3.3)/4096, 3)
        current=round((idadc*2*3.3)/409600, 3)   # current value calculation from 12bit adc, the factor of two is there because there is a divider in the circuit
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")d


        current_log=np.log(current)
        csv_val=','.join([str(voltage),str(current)])
        csv_log_data=','.join([str(voltage),str(current_log)])
        csv_op=open('datapoints.txt','a')
        #print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()
        csv_log=open('logpoints.txt','a')
        csv_log.write(f"{csv_log_data}\n")
        csv_log.close()

    csv_log=open('logpoints.txt','r+')
    lines_log=csv_log.readlines()
    lines_log=[line.strip() for line in lines_log]
    print(type(lines_log))
    csv_log.close()
    csv_log=open('logpoints.txt','w')  # to clear the file contents
    csv_log.close()
    for line in lines_log:
        data_sep=line.split(',')
        vd=float(data_sep[0])
        idlog=float(data_sep[1])
        if (idlog==-math.inf):
            continue 
        csv_log_data=','.join([str(vd),str(idlog)])
        csv_log=open('logpoints.txt','a')
        csv_log.write(f"{csv_log_data}\n")
        csv_log.close()
coord = []
eta=0.0


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
        p20 = np.poly1d(np.polyfit(x, y, 10))   #define polynomial fit order here 

    p = np.polyfit(x_log, y_log, 1)

    print(p)
    eta=round(1000/(p[0]*26),2)
    print(eta)
    xlp=np.linspace(0.3,0.678,180)  #V vs ln(I) curve fitting

    F=(math.exp(p[1]))*(e**(p[0]*xlp))
    ax.plot(x, y, '.',label='experimetal data')
    #ax.plot(x_log, y_log, '+',label='log data')
    xp=np.linspace(0.3,.678,180)   #V vs I curve fitting
    
    ax.plot(xlp, F, 'g',label='linear fit')
    ax.plot( xp, p20(xp), 'r', label='10th order polynomial fit')
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

convert()
plotg()