
void setup() {

  // initialize serial communication at 9600 bits per second:

  Serial.begin(9600);
  pinMode(2, OUTPUT);
}



// the loop routine runs over and over again forever:

void loop() {

  // read the input on analog pin 0:

  float sensorValue = analogRead(A1)*5;

  sensorValue = sensorValue/1024;

  sensorValue = sensorValue - 0.5;

  sensorValue = sensorValue / 0.01;

  // print out the value you read:

  int humidity = analogRead(A0);

  Serial.println(sensorValue);

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
