import serial
import time
import tkinter as tk
from tkinter import ttk 

#ser=serial.Serial('COM9', baudrate=9600, timeout=1)
#i=0
def start():
    ser=serial.Serial('COM9', baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data=open('points.txt','w')
    while(i<67):
        avrdata=ser.readline().decode('ascii')
        data.write(avrdata)
        i=i+1
    data.close()


root=tk.Tk()
root.title("WELCOME TO CURVE TRACER FOR DIODES")
start_button=ttk.Button(root,text="start",command=start)
start_button.pack(side='left', fill='x',expand=True)
quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.pack(side='left', fill='x',expand=True)
#convert_button=ttk.Button(root,text="start",command=start)
#convert_button.pack(side='left', fill='x',expand=True)
root.mainloop()