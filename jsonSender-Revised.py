# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json


ptype = sys.argv[1]
wvalue = sys.argv[2]
tvalue = sys.argv[3]
time = sys.argv[4]
name = sys.argv[5]



#setting up input socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 1006
server_address = ('localhost', port)


#setting up output socket
d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = 1007
sa = ('localhost', p)
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
