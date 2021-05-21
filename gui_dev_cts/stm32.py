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
from scipy.misc import derivative
import fileinput

def start():
    ser=serial.Serial('COM7', baudrate=115200, timeout=1)
    data1=open('message.txt','w')
    avrdata=0

    while (avrdata !='done'):
        if(ser.in_waiting>0):
            avrdata=ser.readline().decode('ascii')
            data1.write(avrdata)

    

    data1.close()
    #popup("Reading process is finished, please proceed!")

start()