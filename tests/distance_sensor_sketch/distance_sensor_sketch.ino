#include <Wire.h>       
#include "Ultrasonic.h"  

#define RANGERPIN 3

Ultrasonic ultrasonic(RANGERPIN);

void setup() {

  Serial.begin(9600);

}

void loop() {

  char _buffer[7];
  int millimeters;

  millimeters = ultrasonic.MeasureInMillimeters();
  delay(10); 

  sprintf( _buffer, "%05u", millimeters );
  

  Serial.println(_buffer); 
}