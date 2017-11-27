import serial, time, datetime, socket
from MonitoringNode import MonitoringNode

#port = '/dev/ttyACM0'
#baud = 9600

#ser = serial.Serial(port, baud)

arduino_readings = [0,3,0,2,0,1,9]

valid_readings = False

A = MonitoringNode(0,0,False,8)
B = MonitoringNode(1,0,False,8)
C = MonitoringNode(2,0,False,8)

data = {}
while True:
    ser.flush()

    arduino_readings = ser.readline().split(b' ')
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

        print(int(A.getTime()), " ", int(B.getTime()), " ", int(C.getTime()))
