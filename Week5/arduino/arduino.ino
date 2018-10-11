void setup() {
  // turn on internal pull-up resistor
  Serial.begin( 9600 );
}

void loop() {
  //Serial.println( analogRead( A0 ) / 4);
  Serial.write(analogRead(A0) / 4);

}


