import serial
import time
def start():
    ser=serial.Serial('COM4', baudrate=9600, timeout=1)
    i=0
    ser.write(b's')
    data=open('points.txt','w')
    while(i<240):
        avrdata=ser.readline().decode('ascii')
        data.write(avrdata)
        i=i+1
    data.close()
    
start()   
