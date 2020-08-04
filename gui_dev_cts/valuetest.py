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
vt=29
def popup(message1):
    window= Tk()
    messagebox.showinfo('System Message', f'{message1}')

    window.deiconify()
    window.destroy()

def planckcalc():
    f=int(frequency.get())
    ev=vt*1.6*(10**-19)
    h=ev/f
    print("Calculated Planck constant", h)
    popup(f"hi{h}, bye{ev}")

root=Tk()
frequency=tk.StringVar()
value_label=ttk.Label(root, text='Enter Frequency of light in Hz:')
value_label.pack(side='top', padx=(0,10))
value_entry=ttk.Entry(root,width=15,textvariable=frequency)
value_entry.pack(side='top')
value_entry.focus()
planck_button=ttk.Button(root,text="verify planck",command=planckcalc)
planck_button.pack(side='top', fill='x',expand=True)
root.mainloop()