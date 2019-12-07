# iPot - The Self Water Plant Monitoring System

	Before proceeding with the installation of this distributed system, configure the network such that the machine running the application, the Front End Pi and the Back End Pi are all connected to the same hotspot. We found that using a mobile hotspot allows bypassing any security.
	Obtain the application source code for the iPot through the “App” branch in the repository. Once the code has been compiled and run on ANdroid studio, the app becomes usable through the emulator. Begin by installing the json database receiver python file, jsonRecieverDatabase_V2.py,  and the json arduino python file, Json-RecArd.py, onto a Raspberry Pi. These files that are installed on this Pi can be found under the “database” branch on the iPot Git repository. Along with the python scripts, the database in the same branch titled, testDb.db, should also be installed as this will allow the user to validate their data. The python scripts can be run by traversing into the files through the terminal and running these commands; 
for jsonRecieverDatabase_V2: 

	sudo python jsonRecieverDatabase_V2.py ipOfDeviceRunningApp PortSendingTo 

for Json-RecArd:

	sudo python json-RecArd.py ipOfBackEndPI PortSendingTo 
  
	Once both of these python files are running on the Front End Pi we are able to set up the Back-End Pi. With reference to Appendix B in this document, wire the sensors and actuator in a similar manner to the Pi that will be the Back End Pi. Proceed to the “Communication” branch of the Git repository and install, jsonSender-Revised.py, and Json_receiver_back.py onto the Pi. Run the python file through the terminal. The command required to run Json_receiver_back.py is:

	sudo python Json_reciver_back.py ipOfFrontEndPI PortSendingTo 

The system is now operational and the results can be seen through the data entries on the database installed on the Front End Pi.

You are ready to step away from your plant and monitor its health and progress through the Android mobile application
