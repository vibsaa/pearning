import serial
import time
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
def plotg():

   # fig = plt.figure(figsize=(8, 6))
   # ax = fig.add_subplot(111, facecolor='#CFFBFF')
    plt.close()
    
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')
    
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        p30 = np.poly1d(np.polyfit(x, y, 30))

    print(p30(69))

    xp=np.linspace(0.2,1.4,180)
    _=plt.plot(x, y, '.', xp, p30(xp), 'g')
    plt.legend()
    plt.show()


plotg()