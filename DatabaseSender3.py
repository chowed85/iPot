import sqlite3
import unittest
import datetime
from sqlite3 import Error
 
 
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

#adds in a rwo to table
def addData(cursor,name,waterSense, tempSense, time):
    cursor.execute("INSERT INTO test VALUES(?, ?, ?, ?) ",(name, waterSense, tempSense, time))

#deletes all table data
def deleteAll(cursor):
    cursor.execute('DELETE FROM test')

#gets a column of table
def getColumn(cursor):
    cursor.execute("""SELECT DISTINCT time FROM test""")
    
    data = cursor.fetchall()
    print(data[0])
    

#gets all data from table  
def getAllData(cursor):
    cursorObj.execute('SELECT * FROM test')
    data = cursorObj.fetchall()
    print(data)
    

 
def main():
    conn = create_connection(r"/Users/owner/Documents/testDb.db")

   
    
    cursorObj = conn.cursor()
    #addData(cursorObj, "John", 599, 434, date)

    getColumn(cursorObj)
    #getAllData(cursorObj)
    deleteAll(cursorObj)
    
    conn.commit()

class tester(unittest.TestCase):
    name = "Michael"
    waterSense = 550
    tempSense = 200
    time = datetime.date(2019, 4, 13)

    conn = create_connection(r"/Users/owner/Documents/testDb.db")
    cursorObj = conn.cursor()

    def testAddData(self):
        addData(self.cursorObj, self.name, self.waterSense, self.tempSense, self.time)
        
        self.cursorObj.execute("""SELECT DISTINCT name FROM test WHERE waterSense = 550""")
        data = self.cursorObj.fetchall()
        print(data[0])
        #self.assertEqual(self.name, data[0])
        #self.conn.commit()
if __name__ == '__main__':
    unittest.main() 
        
