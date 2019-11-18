# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

exit = False

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

while not exit:
   buf, address = d.recvfrom(port)
   if not len(buf):
      break
   buf = int(buf)
   print (buf)
   exit = true

s.shutdown(1)
d.shutdown(1)
return buf
  

