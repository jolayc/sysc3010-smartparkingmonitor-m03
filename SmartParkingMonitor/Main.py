# https://github.com/jolayc/sysc3010-smartparkingmonitor/edit/master/SmartParkingMonitor/Main.py
# @author Osama Rachid

import serial, time, datetime, socket, sys, json
from MonitoringNode import MonitoringNode # general utility class

host = "10.0.0.32" # TO DO
socketport = "5047"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, socketport)

port = '/dev/ttyACM0' # port where arduino is connected
baud = 9600 # arduino baud rate for serial communication

ser = serial.Serial(port, baud) # create Serial object

valid_readings = False # used for 

A = MonitoringNode(0,0,False,8)
B = MonitoringNode(1,0,False,8)
C = MonitoringNode(2,0,False,8)

oldData = {"car arrived A": False,
        "is overlimit A": False,
        "car arrived B": False,
        "is overlimit B": False,
        "car arrived C": False,
        "is overlimit C": False,
      }
changes = [None, None, None, None, None, None]

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
 
        data = {"A1": A.carArrived(),
                "O1": A.isOverlimit(),
                "A2": B.carArrived(),
                "O2": B.isOverlimit(),
                "A3": C.carArrived(),
                "O3": C.isOverlimit(),
        }
    
        newData = data
        
        for key in newData:
            if(newData[key] != oldData[key]):
                if(key == "A1"):
                    changes[0] = new[key]
                if(key == "A2"):
                    changes[2] = new[key]
                if(key == "A3"):
                    changes[4] = new[key]
                if(key == "O1"):
                    changes[1] = new[key]
                if(key == "O2"):
                    changes[3] = new[key]
                if(key == "O3"):
                    changes[5] = new[key]
             JSONString = json.dumps(changes)
             s.sendto(string.encode('utf-8'), server_address)
               
        oldData = data
        
s.shutdown(1)
