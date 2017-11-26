import serial, time
from monitoringnode import MonitoringNode

port = '/dev/ttyACM0'
baud = 9600

ser = serial.Serial(port, baud)

valid_readings = False

A = MonitoringNode(0,0)
B = MonitoringNode(1,0)
C = MonitoringNode(2,0)

overLimitA = False
overLimitB = False
overLimitC = False

data = {}

while True:
    ser.flush()
    # save data from Arduino maintaining the monitoring nodes
    arduino_readings = ser.readline().split(b' ') # [id, distance ..., \r\n]
    
    # check if valid and set flag
    if(len(arduino_readings)==7):
        valid_readings = True
    else:
        valid_readings = False
        
    # process valid readings
    if(valid_readings):
        # set distance of each node
        
        A.setDistance(arduino_readings[1])
        B.setDistance(arduino_readings[3])
        C.setDistance(arduino_readings[5])

        # check if car is within range of each node
            # if within range, set up timers
        #--------------------------------------#
        if(A.carArrived()): # car has arrived
            if(A.getStatus()): # parking space has been occupied
                if(A.isOverlimit()): # check is over time limit
                    overLimitA = True
                else:
                    overLimitA = False
            else: # new car has parked
                A.startTimer()
                A.setStatus(True)
            A.setTimer()
        else: # car has left/parking space is empty
            A.resetTimer()
            A.setStatus(False)
        #--------------------------------------#
        if(B.carArrived()): # car has arrived
            if(B.getStatus()): # parking space has been occupied
                if(B.isOverlimit()): # check is over time limit
                    overLimitB = True
                else:
                    overLimitB = False
            else: # new car has parked
                B.startTimer()
                B.setStatus(True)
            B.setTimer()
        else: # car has left/parking space is empty
            B.resetTimer()
            B.setStatus(False)
        #-------------------------------------#
        if(C.carArrived()): # car has arrived
            if(C.getStatus()): # parking space has been occupied
                if(C.isOverlimit()): # check is over time limit
                    overLimitC = True
                else:
                    overLimitC = False
            else: # new car has parked
                C.startTimer()
                C.setStatus(True)
            C.setTimer()
        else: # car has left/parking space is empty
            C.resetTimer()
            C.setStatus(False)
        #------------------------------------#
        # set up data to send
##        data = {'Car arrived A': A.carArrived(),
##                'Timer A': A.getTimer(),
##                'Overlimit A': A.isOverlimit(),
##                'Car arrived B': B.carArrived(),
##                'Timer B': B.getTimer(),
##                'Overlimit B': B.isOverlimit(),
##                'Car arrived C': C.carArrived(),
##                'Timer C': C.getTimer(),
##                'Overlimit C': C.isOverlimit(),
##                }
        # encode data and send to server side
        data = {'A': A.getTimer(),
                'B': B.getTimer(),
                'C': C.getTimer()

            }
        print(arduino_readings)
