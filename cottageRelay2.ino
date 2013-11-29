#include <Time.h>

  char incomingByte;
  int thisHour;
  int aliveHour;

void setup() {                
  // initialize the digital pins as an output.
  Serial.begin(9600);
  pinMode(4, OUTPUT);  
  pinMode(5, OUTPUT); 
  pinMode(6, OUTPUT); 
  pinMode(7, OUTPUT);
 
}

void loop() {
  thisHour = hour();

  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'm') {
      digitalWrite(7, LOW);
    }
    if (incomingByte == 'M') {
      digitalWrite(7, HIGH);
    }
    
    if (incomingByte == 'w') {
      digitalWrite(6, LOW);
    }
    if (incomingByte == 'W') {
      digitalWrite(6, HIGH);
    }
    
    if (incomingByte == 'b') {
      digitalWrite(5, LOW);
    }
    if (incomingByte == 'B') {
      digitalWrite(5, HIGH);
    }
    if (incomingByte == 'U') {
      aliveHour = (thisHour + 1);
      Serial.print(aliveHour);
    }  
  }
  if (thisHour > aliveHour) {
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
  }
}  

