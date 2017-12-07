# https://github.com/jolayc/sysc3010-smartparkingmonitor/blob/master/SmartParkingMonitor/MonitoringNode.py
# @author Hussein Mourad
import time

class MonitoringNode:
    
	# Constructor
    def __init__(self, ID, distance, occupied, max_range,start,elapsed):
        self.ID = ID
        self.distance = int(distance) # in centimeters
        self.occupied = occupied
        self.max_range = int(max_range) # in centimeters
        self.start = int(start) # start time
        self.elapsed = int(elapsed) # timer value
        
    # Main functions
    
	# @return boolean True if a car has been detected within range, False otherwise
    def carArrived(self):
        return (self.distance > 0 and self.distance <= self.max_range)
    
	# @return boolean True if a car has been parked over the time limit, False otherwise
    def isOverlimit(self):
        return (self.elapsed > 90) #90 is 1:30 in seconds
        # real world scenario would be 900 seconds which is 15:00
    
	# @return boolean True if a car is currently parked, False otherwise
    def isOccupied(self):
        return self.occupied
    
	# Set timer value for node
    def update(self): #starts timer if occupied, reset if not
        if(self.carArrived()):
            if(not self.isOccupied()):
                self.setStart()
                self.setOccupied(True)
            self.setTimer()    
        else:
            self.resetTimer()
            self.setOccupied(False)
    
    # Getters and Setters

	# @return int Distance detected
    def getDistance(self):
        return self.distance
    
    def setDistance(self, distance):
        self.distance = int(distance)
        
    def setTimer(self):
        if(self.start > 0):
            self.elapsed = time.time() - self.start
        else:
            self.elapsed = 0
			
	# @return int Time elapsed
    def getTimer(self):
        return self.elapsed
        
    def setStart(self):
        self.start = time.time()
       
    def setOccupied(self, occupied):
        self.occupied = occupied
        
    # Other
    
    # Reset node timer value
    def resetTimer(self):
        self.elapsed = 0
        self.start = 0
