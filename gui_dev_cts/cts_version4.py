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



fitrange=0.5

#ser=serial.Serial('COM9', baudrate=9600, timeout=1)
#i=0
def start():
    ser=serial.Serial('COM3', baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data1=open('points.txt','w')
    #while(i<240):
    for i in tqdm_gui(range(0,241)):
        avrdata=ser.readline().decode('ascii')
        data1.write(avrdata)
        i=i+1
    data1.close()
    popup("Reading process is finished, please proceed!")
    

def popup(message1):
    window= Tk()
    messagebox.showinfo('System Message', f'{message1}')

    window.deiconify()
    window.destroy()
    
    

def convert():
    csv_data=open('points.txt','r')
    lines=csv_data.readlines()
    csv_data.close()
    #print(lines)
    lines=[line.strip() for line in lines]
    #print(lines)
    csv_op=open('datapoints.txt','w')
    csv_op.close()

    for line in lines:
        data_sep=line.split(',')
        vdadc=int(data_sep[0])
        idadc=int(data_sep[1])
        #print(f" {vdadc} , {idadc} ")
        voltage=vdadc*.00654
        current=((idadc*.00654)/6.67)/4.7
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")
        csv_val=','.join([str(voltage),str(current)])
        csv_op=open('datapoints.txt','a')
        #print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()
def set1():
    fitrange=0.5
def set2():
    fitrange=1.5
def set3():
    fitrange=2.5
def set4():
    fitrange=3.5   
def plotg():
    def func(x, a, b):
        return a*np.exp(b*x)
    def deriv(x):
        return derivative(func,x)

    quadratic = lambda x,p: p[0]*(x**2)+p[1]*x+p[2]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')


    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    #Plot experimental data points
    cursor = Cursor(ax, useblit=False, color='black', linewidth=0.5)
    ax.plot(x, y, 'r+', label='experimental-data')
    fitcoeffs=polyfit(x,y,2)
    print(fitcoeffs)    
       

    xFit = np.arange(0.0, fitrange, 0.01) #PUT MAX VALUE OF RANGE =1.2 FOR 1N4007 &=.53 FOR IN5819
    popt, pcov = curve_fit(func, x, y)
    print(popt)
    print(deriv(1.0))
    #Plot the fitted function
    ax.plot(xFit, func(xFit, *popt), 'g', label='fit params(ae^bx): a=%5.3f, b=%5.3f' % tuple(popt)) 
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()


root=Tk()


root.title("WELCOME TO CURVE TRACER FOR DIODES ")
diode_name=tk.StringVar()
name_label=ttk.Label(root, text='Enter Diode Name:')
name_label.pack(side='left', padx=(0,10))
name_entry=ttk.Entry(root,width=15,textvariable=diode_name)
name_entry.pack(side='left')
name_entry.focus()
start_button=ttk.Button(root,text="start",command=start)
start_button.pack(side='left', fill='x',expand=True)
popup("Don't act oversmart and ruin everything, instead follow the sequence of buttons. After Pressing start button wait for a popup to proceed! ")
convert_button=ttk.Button(root,text="convert",command=convert)
convert_button.pack(side='left', fill='x',expand=True)
menubar=Menu(root)
options=Menu(menubar, tearoff=0)
options.add_command(label="range=0.5", command= set1 )
options.add_command(label="range=1.5", command= set2 )
options.add_command(label="range=2.5", command= set3 )
options.add_command(label="range=3.5", command= set4 )
menubar.add_cascade(label="CurveFit_Range", menu=options)
root.config(menu=menubar)

#options.add_radiobutton(label="range=1.5",variable=fitrange, command= lambda: 1.5 )
#options.add_radiobutton(label="range=2.5",variable=fitrange, command= lambda: 2.5 )



plot_button=ttk.Button(root,text="plot",command=plotg)
plot_button.pack(side='left', fill='x',expand=True)
quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.pack(side='left', fill='x',expand=True)
root.mainloop()