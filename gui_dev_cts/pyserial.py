import serial
ser=serial.Serial('COM9', baudrate=9600, timeout=1)


ser.write(b's')
while(1):
    avrdata=ser.readline().decode('ascii')
    print(avrdata)