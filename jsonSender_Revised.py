# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json
import serial
#import RPi.GPIO as GPIO
from datetime import date

#def readValue(pin):
 #   GPIO.output(pin, GPIO.HIGH)
  #  while(GPIO.input(22) == 0):
   #     #print(GPIO.input(22))
    #    pass
    #GPIO.output(pin,GPIO.LOW)
    #time.sleep(0.5)
    
    
def auto(destIP,ptype,wvalue,tvalue,name,times):


    #port listing
    #1006: app to database
    #1007: database to app
    #1008: backend to database
    #1009: database to back end 


    #setting up serial to read data from arduino
    ser = serial.Serial("/dev/ttyACM0","9600")
    ser.baudrate = 9600

    ser.write(str(wvalue))
    time.sleep(6)
    
    #setup GPIO to let the arduino know when to write
    #GPIO.cleanup()
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(17,GPIO.OUT)
    #GPIO.setup(27,GPIO.OUT)
    #GPIO.setup(22,GPIO.IN)

    outPort = 1008
    inPort = 1007
    #setting up output socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (destIP, outPort)


    #setting up input socket
    d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sa = (destIP, inPort)
    d.bind(("",inPort))
    count =0
    temp = "00000"
    humidity = "00000"
    #read data from arduino
    #temp = ser.readline()
    while(True):
        if(count%(int(times)*10)==0):
            #print(ser.inWaiting())
            #print(ser.in_waiting)
            #while(ser.inWaiting()):
            #readValue(17)
            temp = ser.readline()
                       
            while(temp[0]!='t'):
                #if (ser.inWaiting()>0):
                #time.sleep(1)
                #readValue(17)
                #pinOnOff()
                temp = ser.readline()
      
            #if (ser.inWaiting()):
            #pinOnOff()
          
            #readValue(27)
            humidity = ser.readline()
            while(humidity[0]!='h'):
                #if (ser.inWaiting()>0):
                #time.sleep(1)
                #pinOnOff()
                
                #readValue(27)
                time.sleep(0.5)
                humidity = ser.readline()
            humidity = humidity[1:]
            temp = temp[1:]
            #print(read_ser)
            x = {
               "type": ptype,
               "humidity": humidity,
               "temp": temp,
               "time" : str(date.today()),
               "name" : name
            }
            print(type(x))
            # convert into JSON:
            y = json.dumps(x)
                    

            #    s.sendall(data.encode('utf-8'))
            bytesSent = s.sendto(y.encode('utf-8'), server_address)
            time.sleep(10)
            #print(bytesSent)
            i = 1
            while i<=3:
               buf, address = d.recvfrom(inPort)
               if not len(buf):
                  break
               else:
                  g = int(buf)
                  print(g)
                  if g== 6:
                     break
                  elif g == 7 or g== 8:
                     x = {
                        "type": ptype,
                        "humidity": wvalue,
                        "temp": tvalue,
                        "time" : str(time),
                        "name" : name
                     }
                     

                     # convert into JSON:
                     y = json.dumps(x)
                     s.sendto(y.encode('utf-8'), server_address)
                     i = i+1
                  else:
                     s.sendto(y.encode('utf-8'), server_address)
                  i = i+1
            if i==4:
               print("errorHappened")
               print(g)
            else:
               print("Packet Successful")

    d.close()
