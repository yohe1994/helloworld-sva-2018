int xPin = A1;
int yPin = A0;
int touchPin = 7;

void setup() {
  // turn on internal pull-up resistor
  pinMode( touchPin, INPUT_PULLUP );
  Serial.begin( 9600 );
}

void loop() {
  int flex = analogRead( xPin );
  int resistence = analogRead( yPin );
  int touch = digitalRead( touchPin );

  // print out values
  Serial.write( flex );
  Serial.write( "," );
  Serial.write( resistence );
  Serial.write( "," );
  Serial.write( touch );
  Serial.write( "\n" );

  // wait a little bit
  delay( 30 );
}


