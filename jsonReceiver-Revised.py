
import socket, sys, time,json

host = sys.argv[1]
textport = sys.argv[2]
ptype = sys.argv[3]
wvalue = sys.argv[4]
tvalue = sys.argv[5]
time = sys.argv[6]
name = sys.argv[7]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:

print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

buf, address = s.recvfrom(port)
y = json.loads(buf)

    ptype = y['type']
    wvalue = y['humidity']
    tvalue = y['temp']
    time = y['time']
    name = y['name']

if not len(buf):
        break
print ("Received %s bytes from %s %s: " % (len(buf), address, y ))
print("type: %s, humidity: %s, temp: %s, time: %s, name: %s" ptype, wvalue, tvalue, time, name)

s.shutdown(1)
