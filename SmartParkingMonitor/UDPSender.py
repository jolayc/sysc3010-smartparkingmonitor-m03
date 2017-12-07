# Example fo UDPSender to include with Main.py
# This code was used as a guide, it wasn't actually used in our system
import socket, sys, time, json

host = "134.117.57.197" # replace with static IP of pi, this IP was for a lab machine
textport = "5047" # replace with port number to be used

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

data = {"car arrived": False,
        "is overlimit": False
        }
string = json.dumps(data) # converts dictionary to json string

while 1: 
    s.sendto(string.encode('utf-8'), server_address) # sends json string
    time.sleep(1)
    
s.shutdown(1)
