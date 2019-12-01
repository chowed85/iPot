# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

destIP = sys.argv[1] #IP address of destination
toDevice = sys.argv[2] #indicates what device packet is being sent to 1 for App, 2 for database, 3 for pi
ptype = sys.argv[3]
wvalue = sys.argv[4]
tvalue = sys.argv[5]
time = sys.argv[6]
name = sys.argv[7]

#port listing
#1006: app to database
#1007: database to app
#1008: backend to database
#1009: database to back end 

if wvalue == 1:
   outPort = 1007
   inPort =  1006
elif wvalue = 2:
   outPort = 1009
   inPort = 1008
else:
   outPort = 1008
   inPort = 1009

#setting up output socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (destIP, outPort)


#setting up input socket
d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sa = (destIP, inPort)
d.bind(sa)

x = {
   "type": ptype,
   "humidity": wvalue,
   "temp": tvalue,
   "time" : time,
   "name" : name
}

# convert into JSON:
y = json.dumps(x)
        

#    s.sendall(data.encode('utf-8'))
s.sendto(y.encode('utf-8'), server_address)
i = 1
while i<=3:
   buf, address = d.recvfrom(port)
   if not len(buf):
      time.delay(10)
      buf, address = d.recvfrom(port)
   if not len(buf):
      i = i+1
   else:
      g = int(buf)
      if g== 6:
         break
      elif g == 7 or g== 8:
         x = {
            "type": ptype,
            "humidity": wvalue,
            "temp": tvalue,
            "time" : time,
            "name" : name
         }

         # convert into JSON:
         y = json.dumps(x)
         s.sendto(y.encode('utf-8'), server_address)
         i = i+1
      else:
         s.sendto(y.encode('utf-8'), server_address)


if i==4:
   print(g)
else:
   print("Packet Successful")

   

d.close()
