import sqlite3
import unittest
import datetime
from sqlite3 import Error
 
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

 
#def main():
    #conn = create_connection(r"/Users/owner/Documents/testDb.db")
    #cursorObj = conn.cursor()

    #addData(cursorObj, "John", 599, 434, date)
    #getColumn(cursorObj)
    #getAllData(cursorObj)
    #deleteAll(cursorObj)
    
    #conn.commit()

class tester(unittest.TestCase):

    #instance variables for testing
    name = "Michael"
    waterSense = 550
    tempSense = 200
    time = datetime.date(2019, 4, 13)

    #connects to database
    conn = create_connection(r"/Users/owner/Documents/testDb.db")
    cursorObj = conn.cursor()

    #tests the addData method to see if data can be added into the database
    def testAddData(self):
        addData(self.cursorObj, self.name, self.waterSense, self.tempSense, self.time)
        self.cursorObj.execute("""SELECT DISTINCT name FROM test""")
        data = self.cursorObj.fetchall()
        self.assertEqual(self.name, data[0][0])

    #tests the DeleteAll method to see if it deletes all the data from the database
    def testDeletealldata(self):
        addData(self.cursorObj, self.name, self.waterSense, self.tempSense, self.time)
        deleteAll(self.cursorObj)
        self.cursorObj.execute("""SELECT * FROM test""")
        data = self.cursorObj.fetchall()
        self.assertEqual(0, len(data))

    #tests the getRow method to see if you can get the correct row of data from the database
    def testRowData(self):
        addData(self.cursorObj, self.name, self.waterSense, self.tempSense, self.time)
        data = getRow(self.cursorObj,0)
        self.assertEqual(self.name, data[0])
        self.assertEqual(self.waterSense, data[1])
        self.assertEqual(self.tempSense, data[2])
        self.assertEqual(str(self.time), data[3])

    #tests the deleteRow method to see is you can delete specific rows of data from the database
    def testDeleteRow(self):
        addData(self.cursorObj, self.name, self.waterSense, self.tempSense, self.time)
        deleteRow(self.cursorObj, self.name)
        self.cursorObj.execute("SELECT * FROM test WHERE name like'" + self.name + "'")
        data = self.cursorObj.fetchall()
        self.assertEqual([], data)
        
        
if __name__ == '__main__':
    unittest.main() 
        
