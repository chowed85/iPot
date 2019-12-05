
void setup() {

  // initialize serial communication at 9600 bits per second:

  Serial.begin(9600);
  pinMode(2, OUTPUT);
  //pinMode(5,INPUT);
  //pinMode(6,INPUT);
  //pinMode(8,OUTPUT);


}



// the loop routine runs over and over again forever:

void loop() {
  //Serial.println("Start of Loop");
  static String readString = "800";
  static String appendString = "";
  // read the input on analog pin 0:
  static int setup = 0;
  if (setup == 0){
    while(Serial.available())
    {
      //Serial.println(Serial.available());
      delay(30);
      if(Serial.available()>0){
        char c = Serial.read();
        appendString += c;
      }
    }
    setup +=1;
  }
  
  readString = appendString;
  static int x=0;
  float sensorValue = analogRead(A1)*5;

  sensorValue = sensorValue/1024;

  sensorValue = sensorValue - 0.5;

  sensorValue = sensorValue / 0.01;

  // print out the value you read:

  int humidity = analogRead(A0);
  //if(digitalRead(5) ==HIGH){
    Serial.println("t"+ String(sensorValue));
    //digitalWrite(8,HIGH);
  //}
  delay(100);
  //digitalWrite(8,LOW);
  
  //Serial.flush();
  //if(digitalRead(6) ==HIGH){
    Serial.println("h"+String(humidity));
    //digitalWrite(8,HIGH);
  //}
  delay(100);
  //digitalWrite(8,LOW);
    if(humidity > readString.toInt()){
      digitalWrite(2,HIGH);
    }
    //delay(10000); 
  
    if(humidity < 400){
      digitalWrite(2,LOW);
    }
  //Serial.println("End of Loop");
  delay(100); 
}
