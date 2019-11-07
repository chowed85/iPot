
void setup() {

  // initialize serial communication at 9600 bits per second:

  pinMode(2, OUTPUT);
}



// the loop routine runs over and over again forever:

void loop() {


  digitalWrite(2,HIGH);

  delay(10000); 


  digitalWrite(2,LOW);


  delay(10000); 
}
