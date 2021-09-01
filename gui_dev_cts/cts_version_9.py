import serial
import time
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image  
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
vt=0
phrase='DONE'
coord = []
def start():
    ser=serial.Serial('COM6', baudrate=115200, timeout=1)
    data1=open('points.txt','w')
    avrdata=0
   
    ser.write(b'D')

    while (avrdata !='DONE'):
        if(ser.in_waiting>0):
            avrdata=ser.readline().decode('ascii')
            data1.write(avrdata)

    
    ser.close()
    data1.close()
    return
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
        voltage=round(vdadc*.0081, 3)
        current=round((idadc*.0081)/100, 3)
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

     
    
def plotg():

    
    
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
    
    #l = np.polyfit(x_log, y_log, 1)

    #print(l)
    print(p20(69))
    #xp=np.linspace(-4.5,float(Rangelimit.get()),180)
    
    xp=np.linspace(0,.25,180)
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
    plt.show()
#start()
convert()
#plotg()
