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
        current=(idadc*.00654)/6.67
        #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")
        csv_val=','.join([str(voltage),str(current)])
        csv_op=open('datapoints.txt','a')
        #print(csv_val)
        csv_op.write(f"{csv_val}\n")
        csv_op.close()
    

root=tk.Tk()
root.title("WELCOME TO CURVE TRACER FOR DIODES")
start_button=ttk.Button(root,text="start",command=start)
start_button.pack(side='left', fill='x',expand=True)
quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.pack(side='left', fill='x',expand=True)
convert_button=ttk.Button(root,text="start",command=convert)
convert_button.pack(side='left', fill='x',expand=True)
root.mainloop()