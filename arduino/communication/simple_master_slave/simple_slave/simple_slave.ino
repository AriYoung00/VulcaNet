int byteRead = 0;
void setup(){
 Serial.begin(96//00);
 delay(2000);
}

void loop() {
  /* check if data has been sent from the computer: */
  while (Serial.available()) {
    /* read the most recent byte */
    byteRead = Serial.read(); //now byteRead will have latest sensor 
                              // data sent from Arduino1
  }
  Serial.println(byteRead);
  byteRead++;
  delay(1000);
}
