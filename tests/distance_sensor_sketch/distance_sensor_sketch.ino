#include <Wire.h>       
#include "Ultrasonic.h"  

#define RANGERPIN1 3
#define RANGERPIN2 4

Ultrasonic ultrasonic1(RANGERPIN1);
Ultrasonic ultrasonic2(RANGERPIN2);

void setup() {

  Serial.begin(9600);

}

void loop() {

  char _buffer[7];
  int millimeters1;
  int millimeters2;

  millimeters1 = ultrasonic1.MeasureInMillimeters();
  millimeters2 = ultrasonic2.MeasureInMillimeters();
  delay(10); 

  sprintf( _buffer, "%05u | %05u", millimeters1, millimeters2);
  

  Serial.println(_buffer); 
}