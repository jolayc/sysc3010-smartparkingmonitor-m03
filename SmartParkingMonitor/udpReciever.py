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
    
s.shutdown(1)
