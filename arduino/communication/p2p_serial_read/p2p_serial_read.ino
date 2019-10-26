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
const int inputPin = 0;

//raw reading variable
int inputVal;

void setup()
{
  // start the serial port at 9600 baud
  Serial.begin(9600);
  pinMode(inputPin, INPUT);
}


void loop()
{
 //read the temp sensor and store it in tempVal
 inputVal = analogRead(inputPin);

 //print out the 10 value from analogRead
 Serial.print("Input Val = ");
 Serial.println(inputVal);

 //wait a bit before taking another reading
 delay(500);
}
