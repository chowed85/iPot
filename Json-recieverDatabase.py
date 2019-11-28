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



#setting up input socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 1006
server_address = ('localhost', port)
s.bind(server_address)

#setting up output socket
d= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = 1007
sa = ('localhost', p)


#method for sending response to sender program, acktype is the int code used for responses
def respond(acktype):
    data = str(acktype)
    d.sendto(data.encode('utf-8'), sa)
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
def addData(cursor, name, waterSense, tempSense, time):
    cursor.execute("INSERT INTO test VALUES (?, ?, ?, ?) ", (name, waterSense, tempSense, time))

#deletes all database data
def deleteAll(cursor):
    cursor.execute('DELETE FROM test')

#gets a row of the database
def getRow(cursor, row):
    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()
    return data[row]
    

#gets all data from database 
def getAllData(cursor):
    cursorObj.execute('SELECT * FROM test')
    data = cursorObj.fetchall()
    print(data)

#deletes specific rows of data from the database 
def deleteRow(cursor, name):
    cursor.execute("DELETE FROM test WHERE name like '" + name + "'")

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
    pType = y['type']
    wValue = y['humidity']
    tValue = y['temp']
    date = y['time']
    name = y['name']
    print(pType)
    #pot creation checking for type 7 or type 8 errors
    if pType == 1:
        if wValue == None or time == None or name ==None:
            respond(7)
        if wValue >wMin or time < 0:
            respond(8)
        else:
            respond(6)
    
    #Request for info on a Pot checking for type 7 or type 8 errors
    elif pType == 2:
        if name == None:
            respond(7)
        #have if statment for if name is not in database
        #   respond(8)
        else:
            respond(6) 
            
    #Stored sensor log from database incomplete packet checking for type 7 or type 8 errors
    elif pType==3 or pType ==4 or pType == 5:
        print("test")
        if wValue == None or tValue == None or time == None or name ==None:
            
            respond(7)
        elif lowTemp> tValue or tValue > highTemp or wValue<wMax or wValue>wMin:
            respond(8)
        else:
            addData(cursorObj, name, wValue, tValue ,date)
            print(getAllData(cursorObj))
            respond(6)
    #anything else clause
    else:
        respond(7)
    if dataValid:
        print("type: %s, humidity: %s, temp: %s, time: %s, name: %s",pType, wValue, tValue, time, name)
        dataValid = false
    conn.commit()
s.shutdown(1)

