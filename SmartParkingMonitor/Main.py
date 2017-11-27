# https://github.com/jolayc/sysc3010-smartparkingmonitor/edit/master/SmartParkingMonitor/Main.py
# @author Osama Rachid

import serial, time, datetime, socket
from MonitoringNode import MonitoringNode # general utility class

port = '/dev/ttyACM0' # port where arduino is connected
baud = 9600 # arduino baud rate for serial communication

ser = serial.Serial(port, baud) # create Serial object

valid_readings = False # used for 

A = MonitoringNode(0,0,False,8)
B = MonitoringNode(1,0,False,8)
C = MonitoringNode(2,0,False,8)

data = {}

while True:
    ser.flush() # refresh serial port

    arduino_readings = ser.readline().split(b' ')
    # formatted: [ID, distance, ID, distance, ID, distance, null-terminating char]
    
    if(len(arduino_readings) == 7):
        valid_readings = True
    else:
        valid_readings = False

    if(valid_readings):
        A.setDistance(arduino_readings[1])
        B.setDistance(arduino_readings[3])
        C.setDistance(arduino_readings[5])

        A.update()
        B.update()
        C.update()

       # print(int(A.getTime()), " ", int(B.getTime()), " ", int(C.getTime()))
       # TO-DO: send data to server Pi
