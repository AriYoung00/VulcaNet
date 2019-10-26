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

//analog input pin constant
const int tempPin = 0;

//raw reading variable
int tempVal;

//voltage variable
float volts;

//final temperature variables
float tempC;
float tempF;

void setup()
{
  // start the serial port at 9600 baud
  Serial.begin(9600);
}


void loop()
{
 //read the temp sensor and store it in tempVal
 tempVal = analogRead(tempPin);

 //print out the 10 value from analogRead
 Serial.print("TempVal = ");
 Serial.print(tempVal);

 //print a spacer  
 Serial.print(" **** ");

//wait a bit before taking another reading
delay(1000);
}
