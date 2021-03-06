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
    ser=serial.Serial(COM.get(), baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data1=open('points.txt','w')
    #while(i<240):
    for i in tqdm_gui(range(0,241)):              #this way of reading the values from the serial port is wrong
        avrdata=ser.readline().decode('ascii')    #the method is rectified in future versions of the project.
        data1.write(avrdata)                      #the used method is wrong because instead of polling the serial port when data is available 
        i=i+1                                     #it polls with the loop iteration. same problem is with all the previous versions.
    '''while(i<240):
        avrdata=ser.readline().decode('ascii')
        data1.write(avrdata)
        i=i+1'''
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
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")d
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
        global vt
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        points = tuple(zip(xdata[ind], ydata[ind]))
        slope=(points[-1][1]-points[0][1])/(points[-1][0]-points[0][0])
        rd=1/slope
        vt=points[0][0]-(points[0][1]/slope)
        

        print('onpick points:', points)
        print('slope:', slope)
        print('Dynamic resistance:', rd)
        print('Threshold voltage:', vt)
        popup(f"slope:{slope} , Dynamic resistance:{rd} , Threshold voltage:{vt} ")
        #return vt
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')
        
    #Plot experimental data points
    cursor = Cursor(ax, useblit=False, color='black', linewidth=0.5)
    ax.plot(x, y, 'r+', label='experimental-data')
    fitcoeffs=polyfit(x,y,2)
    print(fitcoeffs)


    xFit = np.arange(0.0, float(Rangelimit.get()) , 0.01) #float(Rangelimit.get())

    popt, pcov = curve_fit(func, x, y)
    print(popt)
    #Plot the fitted function 
    ax.plot(xFit, func(xFit, *popt), 'g', label='fit params(ae^bx): a=%5.3f, b=%5.3f' % tuple(popt), picker=10) 
    fig.canvas.mpl_connect('pick_event', onpick)
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()
    #return vt
def planckcalc():
    f=int(frequency.get())
    ev=vt*1.6*(10**-19)
    h=ev/f
    print("Calculated Planck constant", h)
    popup(f"Calculated planck constant is:{h}")
root=Tk()


root.title("WELCOME TO CURVE TRACER FOR DIODES ")
diode_name=tk.StringVar()
frequency=tk.StringVar()
COM=tk.StringVar()
Rangelimit=tk.StringVar()
#rd=tk.StringVar()
COM_label=ttk.Label(root, text='Enter COM Port in COMx Format:')
COM_label.grid(row=0, column=0,sticky = W, pady = 2)
COM_entry=ttk.Entry(root,width=15,textvariable=COM)
COM_entry.grid(row=0, column=1)
COM_entry.focus()
range_label=ttk.Label(root, text='Enter Curve Fit Range:')
range_label.grid(row=2, column=0,sticky = W, pady = 2)
range_entry=ttk.Entry(root,width=15,textvariable=Rangelimit)
range_entry.grid(row=2, column=1)

name_label=ttk.Label(root, text='Enter Diode Name:')
name_label.grid(row=4, column=0,sticky = W, pady = 2)
name_entry=ttk.Entry(root,width=15,textvariable=diode_name)
name_entry.grid(row=4, column=1)
#name_entry.focus()

start_button=ttk.Button(root,text="start", command=start)
start_button.grid(row=0, column=2, rowspan=5,sticky = tk.N+tk.S)

popup("Don't act oversmart and ruin everything, instead follow the sequence of buttons. After Pressing start button wait for a popup to proceed! ")

convert_button=ttk.Button(root,text="convert",command=convert)
convert_button.grid(row=0, column=3, rowspan=5,sticky = tk.N+tk.S)

plot_button=ttk.Button(root,text="plot",command=plotg)
plot_button.grid(row=0, column=4, rowspan=5,sticky = tk.N+tk.S)

value_label=ttk.Label(root, text='Enter Frequency of light in Hz:')
value_label.grid(row=0, column=6)
value_entry=ttk.Entry(root,width=15,textvariable=frequency)
value_entry.grid(row=0, column=7)

#value_entry.focus()

planck_button=ttk.Button(root,text="verify planck",command=planckcalc)
planck_button.grid(row=2, column=6, columnspan=2,sticky = tk.E+tk.W)

quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.grid(row=4, column=6, columnspan=2,sticky = tk.E+tk.W)
"""T = tk.Text(root, height=4, width=50)
T.pack(side=tk.LEFT, fill=tk.Y)
quote = f"value of dynamic resistance is{rd}"
T.insert(tk.END, quote)"""
root.mainloop()