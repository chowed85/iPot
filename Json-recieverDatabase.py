#!/usr/bin/env python

import MySQLdb
import socket, sys, time,json


db = MySQLdb.connect("localhost", "administrator", "password", "mydb")
db2 = MySQLdb.connect("localhost", "administrator", "password", "Listing")

curs1=db.cursor()
curs2=db2.cursor()

#control variables
Wmin = 425
hightemp = 60
lowtemp = -10
Wmax = 0
dataValid = False

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = 1007
sa = ('localhost', p)
d.bind(sa)

#method for sending response to sender program, acktype is the int code used for responses
def respond(acktype):
    data = str(acktype)
    d.sendto(data.encode('utf-8'), sa)
    if acktype == 6:
        dataValid = True
    

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    y = json.loads(buf)
    if not len(buf):
        break
    print ("Received %s bytes from %s %s: " % (len(buf), address, y ))
    ptype = y['type']
    wvalue = y['humidity']
    tvalue = y['temp']
    time = y['time']
    name = y['name']
    
    curs.execute (INSERT INTO sensor_data VALUES(name, wvalue, tvalue, time))
    
    if dataValid:
        print("type: %s, humidity: %s, temp: %s, time: %s, name: %s" ptype, wvalue, tvalue, time, name)
    
        
        
        
s.shutdown(1)
