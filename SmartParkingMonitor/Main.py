import serial, time, socket, sys, json
from MonitoringNode import MonitoringNode
# @author Osama Rachid

# Static addresses and port numbers
host = "10.0.0.32" # static IP for Server Pi
port = 5069 
arduinoport = '/dev/ttyACM0'
baud = 9600

# Create connection to serial and socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser = serial.Serial(arduinoport, baud)
server_address = (host, port)

# Flag to check if serial readings are valid
valid_readings = False

# Create Parking Monitoring objects
A = MonitoringNode(0,0,False,8,0,0)
B = MonitoringNode(1,0,False,8,0,0)
C = MonitoringNode(2,0,False,8,0,0)

# Set default values to False
# "A" represents carArrived() value
# "O" represents isOverlimit() value
oldData = {"A1": False, # Node A
           "O1": False,
           "A2": False, # Node B
           "O2": False,
           "A3": False, # Node C
           "O3": False
           }

# An array of all changes to data being sent
changes = [False]*6

while True:
	# Flush serial for a fresh reading
    ser.flush()

    arduino_readings = ser.readline().split(b' ')
    
    if(len(arduino_readings) == 7):
        valid_readings = True
    else:
        valid_readings = False
		
	# Process values when 7 elements are detected
    if(valid_readings):
		# Set distances to each node with distances detected by Arduino
        A.setDistance(arduino_readings[1])
        B.setDistance(arduino_readings[3])
        C.setDistance(arduino_readings[5])

		# Update timer values for each node
        A.update()
        B.update()
        C.update()

        # Updated values based on arduino readings
        data = {"A1": A.carArrived(),
           "O1": A.isOverlimit(),
           "A2": B.carArrived(),
           "O2": B.isOverlimit(),
           "A3": C.carArrived(),
           "O3": C.isOverlimit()
           }
		   
        newData = data
		
		# Whenever the new incoming data differs from
		# the old data, record those changes into an array
		# serialize into a JSON String, and send that data
		# to the Server Pi through Socket
        if(newData != oldData):
            for key in newData:
                if(key == "A1"):
                    changes[0] = newData[key]
                if(key == "O1"):
                    changes[1] = newData[key]
                if(key == "A2"):
                    changes[2] = newData[key]
                if(key == "O2"):
                    changes[3] = newData[key]
                if(key == "A3"):
                    changes[4] = newData[key]
                if(key == "O3"):
                    changes[5] = newData[key]
			# Serialize
            JSONString = json.dumps(changes)
            s.sendto(JSONString.encode('utf-8'), server_address)
			
        oldData = newData

s.shutdown(1)
