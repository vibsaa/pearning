# importing tkinter module 
import serial
import time
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
from tqdm import tqdm_gui
from scipy.misc import derivative
# creating tkinter window 
root = Tk() 
i=0
# Progress bar widget 
progress = Progressbar(root, orient = HORIZONTAL, 
			length = 100, mode = 'determinate') 

# Function responsible for the updation 
# of the progress bar value 

        
def start():
    ser=serial.Serial('COM5', baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data1=open('points.txt','w')
    while (i<245):
        avrdata=ser.readline().decode('ascii')
        #time.sleep(.1)
        data1.write(avrdata)
        #time.sleep(.1)
        progress['value']=i
        root.update_idletasks()
        i=i+1
    
    
    data1.close()
    
	

	
	

progress.pack(pady = 10) 

# This button will initialize 
# the progress bar 
Button(root, text = 'Start', command = start).pack(pady = 10) 

# infinite loop 
mainloop() 
