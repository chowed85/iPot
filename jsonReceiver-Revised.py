import socket, sys, time,json
#control variables
Wmin = 700
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
    if ptype == 1:
        #pot creation
        if wvalue == None or tvalue == None or time == None or name ==None:
            respond(7)
        if wvalue <Wmin or time < 0:
            respond(8)
        else:
            respond(6)
    elif ptype == 2:
        if name == None:
            respond(7)
        #have if statment for if name is not in database
        #   respond(8)
        else:
            respond(6)        
    elif ptype==3:
        if wvalue == None or tvalue == None or time == None or name ==None:
            respond(7)
        elif lowtemp> tvalue or tvalue > highvalue or wvalue<Wmax or wvalue>Wmin:
            respond(8)
        else:
            respond(6)
    elif ptype==4:
        if wvalue == None or tvalue == None or time == None or name ==None:
            respond(7)
        elif lowtemp> tvalue or tvalue > highvalue or wvalue<Wmax or wvalue>Wmin:
            respond(8)        
        else:
            respond(6)
    elif ptype == 5:
        if wvalue == None or tvalue == None or time == None or name ==None:
            respond(7)
        elif lowtemp> tvalue or tvalue > highvalue or wvalue<Wmax or wvalue>Wmin:
            respond(8)        
        else:
            respond(6)
    else:
        respond(7)
    if dataValid:
        print("type: %s, humidity: %s, temp: %s, time: %s, name: %s",ptype, wvalue, tvalue, time, name)
    
        
        
        
s.shutdown(1)
