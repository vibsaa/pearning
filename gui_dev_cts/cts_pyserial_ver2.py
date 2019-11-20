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

#ser=serial.Serial('COM9', baudrate=9600, timeout=1)
#i=0
def start():
    ser=serial.Serial('COM9', baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data1=open('points.txt','w')
    while(i<240):
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
    
def plotg():
    #Fitting function
    def func(x, a, b):
        return a*np.exp(b*x)
    #return a*x+b


    style.use('ggplot')
    #Experimental x and y data points   
    x,y = np.loadtxt('datapoints.txt',
                     unpack=True,
                    delimiter = ',')

    #Plot experimental data points
    plt.plot(x, y, 'r+', label='experimental-data')
 
 
 
    #Perform the curve-fit
    popt, pcov = curve_fit(func, x, y)
    print(popt)
 
    #x values for the fitted function   
    xFit = np.arange(0.0, 1.20, 0.01)
 
    #Plot the fitted function
    plt.plot(xFit, func(xFit, *popt), 'g', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
    plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()


root=tk.Tk()
root.title("WELCOME TO CURVE TRACER FOR DIODES")
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
plot_button=ttk.Button(root,text="plot",command=plotg)
plot_button.pack(side='left', fill='x',expand=True)
quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.pack(side='left', fill='x',expand=True)
root.mainloop()