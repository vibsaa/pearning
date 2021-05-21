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

x_data = np.array([.039, .065, .085, .111, .137, .164, .19  ,.222,.242, .268,294, .314])
y_data = np.array([.001,.001,.002 ,.003,.004 ,.005, .006, .008,
 .01,  .012, .014, .039 ])

log_x_data = np.log(x_data)
log_y_data = np.log(y_data)

curve_fit = np.polyfit(x_data, log_y_data, 2)
print(curve_fit)




y = np.exp(curve_fit[0]) * np.exp(curve_fit[1]*x_data)
plt.plot(x_data, y_data, "o")
plt.plot(x_data, y)
plt.show()