import time, datetime

class MonitoringNode:

    # Default values
    start = 0
    elapsed = 0
    
    def __init__(self, ID, distance, occupied, max_range):
        self.ID = ID
        self.distance = distance
        self.occupied = occupied
        self.max_range = max_range
        
    # Main functions
    
    def carArrived(self):
        return (self.distance > 0 and self.distance <= self.max_range)
    
    def isOverlimit(self):
        return (self.elapsed > 900) #900 is 15 mins in seconds 
    
    def isOccupied(self):
        return self.occupied
    
    def update(self): #starts timer if occupied, reset if not 
        return 0
    
    # Getters and Setters

    def getDistance(self):
        return self.distance
    
    def setDistance(self, distance):
        self.distance = distance
        
    def getTimer(self):
        return self.elapsed
        
    def setTimer(self):
        if(self.start > 0):
            self.elapsed = time.time() - self.start
        else:
            self.elapsed = 0

    def setStart(self):
        self.start = time.time()
       
        
    def setOccupied(self, occupied):
        self.occupied = occupied
        
    # Other

    def resetTimer(self):
        self.elapsed = 0
        self.start = 0
