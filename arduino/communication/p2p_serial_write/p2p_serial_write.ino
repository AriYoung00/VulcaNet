/*
SparkFun Inventor's Kit 
Example sketch 07

TEMPERATURE SENSOR

  Use the "serial monitor" window to read a temperature sensor.

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn more about Arduino.

*/

//analog output pin constant
const int outputPin = 0;

//raw reading variable
int outputVal = 0;

void setup()
{
  // start the serial port at 9600 baud
  Serial.begin(9600);
  pinMode(outputPin, OUTPUT);
}


void loop()
{
 //increment outputVal so we read an updated value
 outputVal++;

 analogWrite(outputPin, outputVal);

 //print out the 10 value from analogRead
 Serial.write("Output Val = ");
 Serial.println(outputVal);

 //wait a bit before sending more data
 delay(1000);
}
