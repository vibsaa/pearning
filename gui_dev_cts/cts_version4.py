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
 
def plotg():
    def func(x, a, b):
        return a*np.exp(b*x)

    quadratic = lambda x,p: p[0]*(x**2)+p[1]*x+p[2]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')
    
    def onpick(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        points = tuple(zip(xdata[ind], ydata[ind]))
        slope=(points[-1][1]-points[0][1])/(points[-1][0]-points[0][0])
        rd=1/slope
        vt=points[0][0]-(points[0][1]/slope)
        #print('onpick points:', points)
        print('slope:', slope)
        print('Dynamic resistance:', rd)
        print('Threshold voltage:', vt)
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')
        
    #Plot experimental data points
    cursor = Cursor(ax, useblit=False, color='black', linewidth=0.5)
    ax.plot(x, y, 'r+', label='experimental-data')
    fitcoeffs=polyfit(x,y,2)
    print(fitcoeffs)


    xFit = np.arange(0.0, 3.4, 0.01) #PUT MAX VALUE OF RANGE =1.2 FOR 1N4007 &=.53 FOR IN5819 &=3.5 for LED
    popt, pcov = curve_fit(func, x, y)
    print(popt)
    #Plot the fitted function 
    ax.plot(xFit, func(xFit, *popt), 'g', label='fit params(ae^bx): a=%5.3f, b=%5.3f' % tuple(popt), picker=10) 
    fig.canvas.mpl_connect('pick_event', onpick)
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    #plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()

root=Tk()


root.title("WELCOME TO CURVE TRACER FOR DIODES ")
diode_name=tk.StringVar()
#rd=tk.StringVar()
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
"""T = tk.Text(root, height=4, width=50)
T.pack(side=tk.LEFT, fill=tk.Y)
quote = f"value of dynamic resistance is{rd}"
T.insert(tk.END, quote)"""
root.mainloop()