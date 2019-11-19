

import unittest,socket, sys, time, json

def jsonSenderMock(host,port,tpe,humidity,temp,time,name):
   exit = False
   
   host = host
   textport = port
   ptype = tpe
   wvalue = humidity
   tvalue = temp
   time = time
   name = name
   
   
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
      #print (buf)
      exit = True
   d.shutdown(1)
   s.shutdown(1)
   d.close()
   s.close()
   return buf 


class TestCommProtocol(unittest.TestCase):
    
   def test_type_1_scucess(self):
      print("A successful packet (Int 1) is sent.")
      result = jsonSenderMock('localhost',1006,1,500,None,80,'word')
      self.assertEqual(result, 6)
    
   def test_type_2_scucess(self):
      result = jsonSenderMock('localhost',1006,2,None,None,None,'word')
      self.assertEqual(result, 6)   
    
   def test_type_3_scucess(self):
      result = jsonSenderMock('localhost',1006,3,500,26,80,'word')
      self.assertEqual(result, 6) 
        
   def test_type_4_scucess(self):
      result = jsonSenderMock('localhost',1006,4,500,26,80,'word')
      self.assertEqual(result, 6) 

   def test_type_5_scucess(self):
      result = jsonSenderMock('localhost',1006,5,500,26,80,'word')
      self.assertEqual(result, 6)
        
   def test_type_7_error(self):
      result = jsonSenderMock('localhost',1006,5,None,None,80,'word')
      self.assertEqual(result, 7)
   def test_type_8_error(self):
      result = jsonSenderMock('localhost',1006,5,500,-800000,80,'word')
      self.assertEqual(result, 8)  
if __name__ == '__main__':
   unittest.main()    
    
