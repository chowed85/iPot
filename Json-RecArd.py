import socket, sys, time,json
import sqlite3
import datetime
from sqlite3 import Error

#control variables used for configuration
wMin = 700
highTemp = 60
lowTemp = -10
wMax = 0
dataValid = False

ip = sys.argv[1]
returnport = sys.argv[2]

#setting up input socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int (1008)
server_address = ('', port)
s.bind(server_address)

#setting up output socket
d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = int(returnport)
sa = ((ip, p))


#method for sending response to sender program, acktype is the int code used for responses
def respond(acktype):
    data = bytearray(str(acktype))
    check = d.sendto(data,sa)
    print(acktype)
    print("responded")
    if acktype == 6:
        dataValid = True

#creates the connecction with the database
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        
    except Error as e:
        print(e)
    #finally:
        #if conn:
            #conn.close()
 
    return conn

#adds in a row of data to the database
def addDataList(cursor, name, wSP, tSP ,interval):
    cursor.execute("INSERT INTO iPotListing VALUES (?, ?, ?, ?) ", (name, wSP, tSP ,interval))

#adds in a row of data to the database
def addDataSensor(cursor, name, waterSense, tempSense, time):
    cursor.execute("INSERT INTO SensorData VALUES (?, ?, ?, ?) ", (name, waterSense, tempSense, time))

#deletes all database data
def deleteAll(cursor):
    cursor.execute('DELETE FROM SensorData')

#gets a row of the database
def getRow(cursor, dname):
    cursor.execute("SELECT * FROM SensorData WHERE name like '" + dname + "'")
    data = cursor.fetchall()
    return data
    

#gets all data from database 
def getAllData(cursor):
    cursorObj.execute('SELECT * FROM SensorData')
    data = cursorObj.fetchall()
    print(data)

#deletes specific rows of data from the database 
def deleteRow(cursor, name):
    cursor.execute("DELETE FROM SensorData WHERE name like '" + name + "'")

while True:
    #connection for database
    conn = create_connection(r"/home/pi/Documents/testDb.db")
    cursorObj = conn.cursor()
    
    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    
    #loads the info from the input port and load the json into variables
    buf, address = s.recvfrom(port)
    y = json.loads(buf)
    if not len(buf):
        break
    print ("Received %s bytes from %s %s: " % (len(buf), address, y ))
    pType = int(y['type'])
    wValue = int(y['humidity'])
    tValue = float(y['temp'])
    time = y['time']
    name = y['name']
    #lots of test code
    #print(pType)
    #print(time)
    #print(wValue)
    #print(type(wValue))
    #pot creation checking for type 7 or type 8 errors
    if pType == 1:
        if not wValue or len(time) == 0 or name is None:
            respond(7)
            #print("A")
        elif float(wValue) > wMin:
            respond(8)
            #print("b")
        else:
            respond(6)
            #print("there should be a resoinse")
            addDataList(cursorObj, name, wValue, tValue ,time)
            #print(getAllData(cursorObj))
    
    #Request for info on a Pot checking for type 7 or type 8 errors
    elif pType == 2:
        if name == None:
            respond(7)
        #have if statment for if name is not in database
        #   respond(8)
        else:
            respond(6)
            print(getRow(cursorObj, name))
    
            potData = getRow(cursorObj, name)
            
            for row in potData:
                print(row)
                print(row[1])
                #for i in range(len(row)):

                ptype = 3
                wvalue = row[1]
                tvalue = row[2]
                time = row[3]
                name = row[0]                    
                
                x = {
                   "type": ptype,
                   "humidity": wvalue,
                   "temp": tvalue,
                   "time" : time,
                   "name" : name
                 }
                    
                
                y = json.dumps(x)
                d.sendto(y.encode('utf-8'),sa)
            respond(4)
             
            
    #Stored sensor log from database incomplete packet checking for type 7 or type 8 errors
    elif pType==3 or pType ==4 or pType == 5:
        print("test")
        if wValue == None or tValue == None or time == None or name ==None:
            
            respond(7)
        elif lowTemp> tValue or tValue > highTemp or wValue<wMax or wValue>wMin:
            respond(8)
        else:
            if pType == 5:
                addDataSensor(cursorObj, name, wValue, tValue ,time)
                #print(getAllData(cursorObj))
            respond(6)
    #anything else clause
    else:
        print("improper paket")
        respond(7)
    if dataValid:
        print("type: %s, humidity: %s, temp: %s, time: %s, name: %s",pType, wValue, tValue, time, name)
        dataValid = false
    conn.commit()
s.shutdown(1)



