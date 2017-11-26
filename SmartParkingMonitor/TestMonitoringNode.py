import time, datetime
from MonitoringNode import MonitoringNode

A = MonitoringNode(0, 5, False, 8)

time.sleep(1)
A.setStart()
    
while True:
    A.setTimer()
    if(A.getTimer() > 5):
        A.resetTimer()
        A.setStart()
    print(A.getTimer())
