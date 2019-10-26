//raw reading variable
int outputVal = 0;

void setup(){
 Serial.begin(9600);
 delay(2000);
}

void loop() {
 ////read sensor data to a variable 
 Serial.println(outputVal);
 outputVal++;
 delay(2000); //Not to flood serial port
}
