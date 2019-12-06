# iPot
T11's Sysc3010 Project

AllHardware.ino this is the arduino code that was being run during the final presentation, this programs includes all the code for reading the sensors and exporting the information, setting the humidity setpoint of the iPot, and controlling the pump based on the humidity level and set point

Json_receiver_back.py this is the program used to recive initialization data from the app and it sets the setpoints for the arduino, after that is done it calls the next program listed

jsonSender_Revised.py this program will automatically read the data from the sensor and then pacakge and send that information to the database so that it can be stored

Sensors.ino test code designed to only monitor the sensors and make sure they are functioning successfully

onlyPump.ino test code used to toggle the pump on and off using arduino control
