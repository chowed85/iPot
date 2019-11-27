# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
ptype = sys.argv[2]
wvalue = sys.argv[3]
tvalue = sys.argv[4]
time = sys.argv[5]
name = sys.argv[6]



#setting up input socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, 1006)


#setting up output socket
d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = 1007
sa = (host, p)
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
      g=json.loads(buf)
      if g["type"] == 6:
         break
      elif g["type"] == 7 or g["type"] == 8:
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
   print("there was a type " + g["type"] + "error with the packet")
else:
   print("Packet Successful")

   

d.shutdown(1)
d.close()
