void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  float sensorValue = analogRead(A0)*5;
  sensorValue = sensorValue/1024;
  sensorValue = sensorValue - 0.5;
  sensorValue = sensorValue / 0.01;
  // print out the value you read:
  int humidity = analogRead(A1);
  Serial.println(sensorValue);
  Serial.println(humidity);
  delay(100);        // delay in between reads for stability
}
