int humVal;


void setup() {

  // initialize serial communication at 9600 bits per second:

  Serial.begin(9600);
  pinMode(2, OUTPUT);

  
}



// the loop routine runs over and over again forever:

void loop() {

  // read the input on analog pin 0:
  
  
  // print out the value you read:
  Serial.println(sensorValue);
  
  int humidity = analogRead(A0);
  

  //method testing
  if(testAir(humidity)){
	Serial.println('PASS: The humidity is within range of 540 - 560 which is the expected value');
	Serial.println('The value is: ' + humidity);
  }
  
  else{
	Serial.println('FAIL: The humidity is not within range of 540 - 560 which is the expected value');
	Serial.println('The value is: ' + humidity);
  }
  
  delay(10000);
  
  humVal = analogRead(A0)

  Serial.println('The value of the soil without water is: ' + humVal);
  
  delay(10000);
  
  humidity = analogRead(A0)
  
  if(testValueDecrease(humidity))
	Serial.println('PASS: The humidity value is less than before');
	Serial.println('The value is: ' + humidity);
  }
  
  else{
	Serial.println('FAIL: The humidity value is not less than before');
	Serial.println('The value is: ' + humidity);  
  }
  
  
  delay(10000);
  
  if(testValueIncrease(humidity))
	Serial.println('PASS: The humidity value is greater than the soil');
	Serial.println('The value is: ' + humidity);
  }
  
  else{
	Serial.println('FAIL: The humidity value is not greater than the soil');
	Serial.println('The value is: ' + humidity);  
  }
  

  delay(10000); 
}

//testing dry air
private boolean testAir(int humidity){
  if (humidity>=540 && humidity<= 560){
    return true;  
  }
}

//sensor goes from dry soil to damp soil 
private boolean testValueDecrease(int humidity){
  if (humidity < humVal){
    return true; 
  }
  return false;
}

//when sensor goes from soil to air
private boolean testValuIncrease(int humidity){
  if (humidity > humVal){
    return true; 
  }
  return false;
}
