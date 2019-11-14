# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]
ptype = sys.argv[3]
wvalue = sys.argv[4]
tvalue = sys.argv[5]
time = sys.argv[6]
name = sys.argv[7]


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)


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
   else:
      g=json.loads(buf)
      if g["type"] == 6:
         break
      elif g["type"] == 7 or g["type"] == 8:
         #repack data from args into x here
      else:
         s.sendto(y.encode('utf-8'), server_address)
   i+=i

if i==4:
   print("there was a type " + g["type"] + "error with the packet")

   

s.shutdown(1)

