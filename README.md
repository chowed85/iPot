# iPot
T11's Sysc3010 Project
CommTest.py is the testing program used to check the communication code that we used in the project. It used code from jsonSenderMock.py to create a cut down sender method to see if proper replies to packets were sent at a local level

DatabaseSender3.py is the test program used to test database functionality. It opens up test.db locally and then tests adding and removing data from it and verifying that the operations were done sucessfully

Hardware_testing.ino is used to check that each of the sensors were functioning properly and giving the correct values when used

hardware_stub_testing.ino was used to check if it was possible to write values to the arduino and checking whether or not the pump would function properly given the correct inputs

jsonSenderMock.py contains code used in devloping the CommTest message send method

testDb.db test database used in the database tests
