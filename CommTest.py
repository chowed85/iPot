import jsonSenderMock

import unittest

class TestCommProtocol(unittest.TestCase):
    
    def test_type_1_scucess(self):
        result = jsonSenderMock('localhost',1006,1,500,None,80,word)
        self.assertEqual(result, 6)
    
    def test_type_2_scucess(self):
        result = jsonSenderMock('localhost',1006,2,None,None,None,word)
        self.assertEqual(result, 6)   
    
    def test_type_3_scucess(self):
        result = jsonSenderMock('localhost',1006,3,500,26,80,word)
        self.assertEqual(result, 6) 
        
    def test_type_4_scucess(self):
        result = jsonSenderMock('localhost',1006,4,500,26,80,word)
        self.assertEqual(result, 6) 

    def test_type_5_scucess(self):
        result = jsonSenderMock('localhost',1006,5,500,26,80,word)
        self.assertEqual(result, 6) 
