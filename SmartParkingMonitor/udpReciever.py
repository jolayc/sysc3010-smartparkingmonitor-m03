import socket, sys, time, json

textport = 5047

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ("", port)
s.bind(server_address)

while True:

    #print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(2048)
    if not len(buf):
        break
    #print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))
    data = json.loads(buf)
    #print (data)
    print (data["car arrived"])
    a = data["car arrived"]
    b = data["is overlimit"]
    arrived = 0
    overlimit = 0   
    
    if a == True:
        arrived = arrived + 1
        #write a to database
    if b == True:
        overlimit = overlimit + 1
        #write b to database
        
   
s.shutdown(1)
