import serial
import time
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image  
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
vt=0
phrase='DONE'
coord = []
def start():
    ser=serial.Serial(COM.get(), baudrate=115200, timeout=1)
    data1=open('points.txt','w')
    avrdata=0
    progress['value']=0
    root.update_idletasks()
    ser.write(b'D')

    while (avrdata !='DONE'):
        if(ser.in_waiting>0):
            avrdata=ser.readline().decode('ascii')
            data1.write(avrdata)

    progress['value']=100
    root.update_idletasks()    
    ser.close()
    data1.close()
    #popup("Reading process is finished, please proceed!")
    
    
    

def popup(message1):
    window= Tk()
    messagebox.showinfo('System Message', f'{message1}')

    window.deiconify()
    window.destroy()

def convert():
    for line in fileinput.input('points.txt', inplace=True):
        if phrase in line:
            continue
        print(line, end='')
    csv_data=open('points.txt','r')
    lines=csv_data.readlines()
    csv_data.close()
    #print(lines)
    lines=[line.strip() for line in lines]
    #print(lines)
    csv_op=open('datapoints.txt','w')
    csv_op.close()
    csv_log=open('logpoints.txt','w')
    csv_log.close()

    
    res = []
    [res.append(x) for x in lines if x not in res]
  
        # printing list after removal 
    #print ("The list after removing duplicates : " + str(res))
    for line in res:
        data_sep=line.split(',')
        vdadc=int(data_sep[0])
        idadc=int(data_sep[1])
        #print(f" {vdadc} , {idadc} ")
        voltage=round((vdadc*3.3)/4096, 3)
        current=round((idadc*2*3.3)/409600, 3)   # current value calculation from 12bit adc, the factor of two is there because there is a divider in the circuit
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")d


        current_log=np.log(current)
        csv_val=','.join([str(voltage),str(current)])
        csv_log_data=','.join([str(voltage),str(current_log)])
        csv_op=open('datapoints.txt','a')
        #print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()
        csv_log=open('logpoints.txt','a')
        csv_log.write(f"{csv_log_data}\n")
        csv_log.close()

     
    


def plotg():

    
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#CFFBFF')
        
    x,y = np.loadtxt('datapoints.txt',
                    unpack=True,
                    delimiter = ',')

    x_log,y_log = np.loadtxt('logpoints.txt',
                    unpack=True,
                    delimiter = ',')
    
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        p20 = np.poly1d(np.polyfit(x, y, 10))
    
    #l = np.polyfit(x_log, y_log, 1)

    #print(l)
    print(p20(69))
    #xp=np.linspace(-4.5,float(Rangelimit.get()),180)
    
    xp=np.linspace(0.3,float(Rangelimit.get()),180)
    ax.plot(x, y, '.',label='experimetal data')
    ax.plot( xp, p20(xp), 'r', label='fitted data')
    # Defining the cursor
    cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = 'b', linewidth = .5)
# Creating an annotating box
    annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox=dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
    annot.set_visible(False)
# Function for storing and showing the clicked values
    
    def onclick(event):
        global coord
        coord.append((event.xdata, event.ydata))
        x = event.xdata
        y = event.ydata
        print([x,y])
        annot.xy = (x,y)
        text = "({:.2g},{:.2g})".format( x,y )
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw() #redraw the figure
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title(f'CHARACTERSTIC CURVE FOR {diode_name.get()}')
    plt.xlabel('Vd(volts)')
    plt.ylabel('Id(amperes)')
    plt.legend()
    plt.show()
    


def planckcalc():
    f=int(frequency.get())
    ev=vt*1.6*(10**-19)
    h=ev/f
    print("Calculated Planck constant", h)
    popup(f"Calculated planck constant is:{h}")
    
def sch():
    root1 = Tk()  
    imgsch = PhotoImage(file = r"H:\pearning_official\sch.png", master=root1)
    imgsche = imgsch.subsample(1, 1)
  
# setting image with the help of label
    Label(root1, image = imgsche).grid(row = 10, column = 0,
       columnspan = 8, rowspan = 8)
    root1.mainloop()
def board():
    root1 = Tk()  
    imgsch = PhotoImage(file = r"H:\pearning_official\board.png", master=root1)
    imgsche = imgsch.subsample(1, 1)
  
# setting image with the help of label
    Label(root1, image = imgsche).grid(row = 10, column = 0,
       columnspan = 8, rowspan = 8)
    root1.mainloop()

        
    

root=Tk()
root.title("WELCOME TO CURVE TRACER")
diode_name=tk.StringVar()
frequency=tk.StringVar()
COM=tk.StringVar()
Rangelimit=tk.StringVar()
Mode=tk.StringVar()

COM_label=ttk.Label(root, text='Enter COM Port in COMx Format:', font=('Arial Rounded MT Bold', 8))
COM_label.grid(row=0, column=0,sticky = W, pady = 2)
COM_entry=ttk.Entry(root,width=15,textvariable=COM)
COM_entry.grid(row=0, column=1)
COM_entry.focus()

range_label=ttk.Label(root, text='Enter Curve Fit Range:',font=('Arial Rounded MT Bold', 8) )
range_label.grid(row=2, column=0,sticky = W, pady = 2)
range_entry=ttk.Entry(root,width=15,textvariable=Rangelimit)
range_entry.grid(row=2, column=1)

Mode_label=ttk.Label(root, text='Select Operating Mode(D,C,L,R)',font=('Arial Rounded MT Bold', 8) )
Mode_label.grid(row=4, column=0,sticky = W, pady = 2)
Mode_entry=ttk.Entry(root,width=15,textvariable=Mode)
Mode_entry.grid(row=4, column=1)

name_label=ttk.Label(root, text='Enter Component Name:',font=('Arial Rounded MT Bold', 8) )
name_label.grid(row=6, column=0,sticky = W, pady = 2)

progress = Progressbar(root, orient = HORIZONTAL, 
			length = 100, mode = 'determinate') 
progress.grid(row=6, column=2, columnspan=6, sticky = tk.E+tk.W, pady = 2)

name_entry=ttk.Entry(root,width=15,textvariable=diode_name)
name_entry.grid(row=6, column=1)

startim = PhotoImage(file = r"H:\pearning_official\power.png")
startimg=startim.subsample(8,8)

start_button=Button(root,image=startimg,border=0,compound='top',text="Start",font=('Britannic Bold', 10) ,bg='white',activebackground='lime green', command=start)
start_button.grid(row=0, column=2, rowspan=5,sticky = tk.N+tk.S)


popup("Don't act oversmart and ruin everything, instead follow the sequence of buttons. After Pressing start button wait for a popup to proceed! ")
conim = PhotoImage(file = r"H:\pearning_official\convert.png")
cimg=conim.subsample(8,8)
convert_button=Button(root,text="Convert",image=cimg,border=0,compound='top',font=('Britannic Bold', 10) , bg='white',activebackground='blue',command=convert)
convert_button.grid(row=0, column=3, rowspan=5,sticky = tk.N+tk.S)
gim = PhotoImage(file = r"H:\pearning_official\graphic.png")
gimg=gim.subsample(8,8)
plot_button=Button(root,text="Plot",image=gimg,compound='top',border=0,font=('Britannic Bold', 10) , bg='white',activebackground='deep pink',command=plotg)
plot_button.grid(row=0, column=4, rowspan=5,sticky = tk.N+tk.S)

value_label=ttk.Label(root, text='Enter Frequency of light in Hz:',font=('Arial Rounded MT Bold', 8) )
value_label.grid(row=0, column=6)
value_entry=ttk.Entry(root,width=15,textvariable=frequency)
value_entry.grid(row=0, column=7)


planck_button=Button(root,text="Verify Planck",font=('Britannic Bold', 10) ,bg='white',activebackground='orange',command=planckcalc)
planck_button.grid(row=2, column=6, columnspan=2,sticky = tk.E+tk.W)

showsch_button=Button(root,text="Show Schematic",font=('Britannic Bold', 10) ,bg='white',activebackground='lightblue3',command=sch)
showsch_button.grid(row=8, column=0, columnspan=8,sticky = tk.E+tk.W)
showsch_button=Button(root,text="Show Board",font=('Britannic Bold', 10) ,bg='white',activebackground='lightblue3',command=board)
showsch_button.grid(row=10, column=0, columnspan=8,sticky = tk.E+tk.W)
quit_button=Button(root,text='Kill',font=('Britannic Bold', 10) ,bg='white',activebackground='firebrick4',command=root.destroy)
quit_button.grid(row=4, column=6, columnspan=2,sticky = tk.E+tk.W)


root.mainloop()