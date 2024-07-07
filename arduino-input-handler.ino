void setup() {
  pinMode(22, OUTPUT); 
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();
    if (input == '0') {
      digitalWrite(22, LOW);
    } else {
      digitalWrite(22, HIGH);
    }
  }
}