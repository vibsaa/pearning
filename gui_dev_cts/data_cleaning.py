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
import warnings
def convert():
    for line in fileinput.input('points.txt', inplace=True):
        if phrase in line:
            continue
        print(line, end='')
    csv_data=open('points.txt','r')
    lines=csv_data.readlines()
    csv_data.close()
    print(lines)
    lines=[line.strip() for line in lines]
    print(lines)
    csv_op=open('datapoints.txt','w')
    csv_op.close()

    for line in lines:
        data_sep=line.split(',')
        vdadc=int(data_sep[0])
        idadc=int(data_sep[1])
        print(f" {vdadc} , {idadc} ")
        voltage=round(vdadc*.00654, 3)
        current=round(((idadc*.00654)/6.67)/4.7, 3)
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")d
        csv_val=','.join([str(voltage),str(current)])
        csv_op=open('datapoints.txt','a')
        print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()
 

convert()