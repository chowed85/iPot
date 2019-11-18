int humVal;


void setup() {

  // initialize serial communication at 9600 bits per second:

  Serial.begin(9600);
  pinMode(2, OUTPUT);

  humval = analogRead(A0);
  
}



// the loop routine runs over and over again forever:

void loop() {

  // read the input on analog pin 0:

  float sensorValue = analogRead(A1)*5;

  sensorValue = sensorValue/1024;
  sensorValue = sensorValue - 0.5;
  sensorValue = sensorValue / 0.01;
  
  
  // print out the value you read:
  Serial.println(sensorValue);
  
  int humidity = analogRead(A0);
  

  //method testing
  //Serial.println(testAir(humidity));
  //humidity = testPumponsim();
  //humidity = testPumpoffsim();
  //Serial.println(testValuedecrease(humidity)); 
  //Serial.println(testValueincrease(humidity));

  Serial.println(humidity);
  
  if(humidity > 525){
    digitalWrite(2,HIGH);
  }
  //delay(10000); 

  if(humidity < 400){
    digitalWrite(2,LOW);
  }

  delay(100); 
}

//testing dry air
private boolean testAir(int humidity){
  if (humidity>=540 && humidity<= 560){
    return true;  
  }
}

//simulated reading of 600
private int testPumponsim(){
  return 600;
}

//simulated reading of 350
private int testPumpoffsim(){
  return 350;
}

//sensor goes from dry soil to damp soil 
private boolean testValuedecrease(int humidity){
  if (humidity < humVal){
    return true; 
  }
  return false;
}

//when sensor goes from soil to air
private boolean testValueincrease(int humidity){
  if (humidity > humVal){
    return true; 
  }
  return false;
}
