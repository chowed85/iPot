
void setup() {

  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}



// the loop routine runs over and over again forever:

void loop() {



  if(testPumpOnSim()> 525){
    digitalWrite(2,HIGH);
    Serial.println('PASS: The pump has turned on because the value simulated is higher than the threshold of 525);
    Serial.println('The stub value is: ' testPumpOnSim());
  }
  
  else{
	Serial.println('PASS: The pump has not turned on because the value simulated is lower than the threshold of 525);
    Serial.println('The stub value is: ' testPumpOnSim());
  }
  
  
  delay(10000); 

  if(testPumpOffSim()< 375){
    digitalWrite(2,LOW);
    Serial.println('PASS: The pump has turned off because the value simulated is lower than the threshold of 375);
    Serial.println('The stub value is: ' testPumpOffSim());
  }
  
  else{
	Serial.println('PASS: The pump has not turned off because the value simulated is lower than the threshold of 525);
    Serial.println('The stub value is: ' testPumpOffSim());
  }

  delay(10000); 
}





//simulated reading of 600
private int testPumponsim(){
  return 600;
}

//simulated reading of 350
private int testPumpoffsim(){
  return 350;
}
