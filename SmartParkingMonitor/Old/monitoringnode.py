import time, datetime

class MonitoringNode:
    max_range = '8' # max range of detection
    timer_string = '0' # time park (string)
    status = False # occupied or vacant
    start_time = 0 # when timer started
    elapsed = 0 # time elapsed
    
    def __init__(self, ID, distance): # constructor
        self.ID = ID
        self.distance = distance

    def carArrived(self):
        return (self.distance > '0' and self.distance <= self.max_range)
    
    def getID(self): # ID of node
        return self.ID
        
    def startTimer(self): # start timer of node
        self.start_time = time.time()
        
    def resetTimer(self): # reset timer of node
        self.timer_string = '0'

    def getTimerNonString(self): # get raw timer in seconds
        return self.elapsed
    
    def setTimer(self): # set timer of node
        elapsed = time.time() - self.start_time
        self.timer_string = str(datetime.timedelta(seconds=elapsed))

    def getTimer(self): # return node timer
        return self.timer_string

    def setDistance(self, distance): # set distance detected of node
        self.distance = str(distance)

    def getDistance(self): # return distance detected
        return self.distance

    def setStatus(self, status):
        self.status = status
        
    def getStatus(self): # return vacant or occupied (over time)
        return self.status
    
    def isOverlimit(self):
        return (self.elapsed > 900)
    
