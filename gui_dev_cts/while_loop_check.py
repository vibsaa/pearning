'''the following method is employed in polling the serial port:
it uses serial library command [in_waiting] to check the size of the incoming data buffer and when the size is >0
the data is fetched continuosly by the [readline] command till {nextline} is encountered.
'''
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
vt=0
def start():
    ser=serial.Serial('COM5', baudrate=9600, timeout=1)
    data1=open('newp1.txt','w')
    avrdata=0
    ser.write(b's')
    
    '''while(ser.readline().decode('ascii')!='DONE'):
        avrdata=ser.readline().decode('ascii')
        
        data1.write(avrdata)
    
    avrdata=ser.read(21000).decode('ascii')
    data1.write(avrdata)    
    data1.close()
    popup("Reading process is finished, please proceed!")'''

    while (avrdata !='DONE'):
        if(ser.in_waiting>0):
            avrdata=ser.readline().decode('ascii')
            data1.write(avrdata)

        

    data1.close()
    exit()


start()