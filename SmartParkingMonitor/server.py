
# Source: https://pymotw.com/2/socket/udp.html
#!/usr/bin/python
print("Content-Type: text/html")
print()

import pymysql, socket, sys, time, json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 5069
server_address = ('', port)
s.bind(server_address)

conn  = pymysql.connect(db='parking',user='root',passwd='root',host='localhost')
cur = conn.cursor()
##c.execute("INSERT INTO spots1(id,parked,overtime) VALUES (1, true, false)")
##c.execute("INSERT INTO spots1(id,parked,overtime) VALUES (2, false, false)")
##c.execute("INSERT INTO spots1(id,parked,overtime) VALUES (3, false, false)")
##
cur.execute("SELECT * FROM spots")
##"""c.execute("commit")"""
##""""""
a='0'
b='0'
c='0'
d='0'
e='0'
f='0'
while True:
    buf, address = s.recvfrom(2048)
    if not len(buf):
        break
    stuff = json.loads(buf.decode('utf-8'))
    print(stuff)
##    data = json.loads(buf)
##    print(data)
##
##
##    print(buf)
##    print(buf[1])
    
    """print(data)"""
    elem1 = stuff[0]
    elem2 = stuff[1]
    elem3 = stuff[2]
    elem4 = stuff[3]
    elem5 = stuff[4]
    elem6 = stuff[5]
    

    if elem1 == True:
        a = int(a) +1
        a = str(a)
        cur.execute("UPDATE spots1 SET parked= true WHERE id = 1")
        cur.execute("UPDATE spots SET parked = %s WHERE id = 1", (a))
    if elem2 == True:
        b = int(b) +1
        b = str(b)
        cur.execute("UPDATE spots1 SET overtime = true WHERE id = 1")
        cur.execute("UPDATE spots SET overtime = %s WHERE id = 1", (b))
    if elem3 == True:
        c = int(c) +1
        c = str(c)
        cur.execute("UPDATE spots1 SET parked = true WHERE id = 2")
        cur.execute("UPDATE spots SET parked = %s WHERE id = 2", (c))
    if elem4 == True:
        d = int(d) +1
        d = str(d)
        cur.execute("UPDATE spots1 SET overtime = true WHERE id = 2")
        cur.execute("UPDATE spots SET overtime = %s WHERE id = 2", (d))
    if elem5 == True:
        e = int(e) +1
        e = str(e)
        cur.execute("UPDATE spots1 SET parked = true WHERE id = 3")
        cur.execute("UPDATE spots SET parked = %s WHERE id = 3", (e))
    if elem6 == True:
        f = int(f) +1
        f = str(f)
        cur.execute("UPDATE spots1 SET overtime = true WHERE id = 3")
        cur.execute("UPDATE spots SET overtime = %s WHERE id = 3", (f))
    if elem1 == False:
       
        cur.execute("UPDATE spots1 SET parked= false WHERE id = 1")
    if elem2 == False:
        
        cur.execute("UPDATE spots1 SET overtime = false WHERE id = 1")
    if elem3 == False:
        
        cur.execute("UPDATE spots1 SET parked = false WHERE id = 2")
    if elem4 == False:
        
        cur.execute("UPDATE spots1 SET overtime = false WHERE id = 2")
    if elem5 == False:
        
        cur.execute("UPDATE spots1 SET parked = false WHERE id = 3")
    if elem6 == False:
        
        cur.execute("UPDATE spots1 SET overtime = false WHERE id = 3")
    cur.execute("commit")
##
s.shutdown(1)
"""
a = c.fetchall();
print(a)
print([(r[0], r[1], r[2]) for r in c.fetchall()])
"""
