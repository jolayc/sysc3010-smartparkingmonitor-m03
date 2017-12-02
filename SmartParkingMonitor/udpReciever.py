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

    print (data)
    elem1 = data[0]
    elem2 = data[1]
    elem3 = data[2]
    elem1 = data[0]
    elem2 = data[1]
    elem3 = data[2]
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0

    if elem1 == True:
        a = a+1
        #UPdate database
    if elem2 == True:
        b = b+1
        #UPdate database
    if elem2 == True:
        c = c+1
        #UPdate database
    if elem2 == True:
        d = d+1
        #UPdate database
    if elem2 == True:
        e = e+1
        #UPdate database
    if elem2 == True:
        f = f+1
        #UPdate database
    print(elem1)
    print(elem2)
    print(elem3)
    
s.shutdown(1)

