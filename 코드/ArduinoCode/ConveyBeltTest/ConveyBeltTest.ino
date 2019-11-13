#include <SoftwareSerial.h>
#include <Servo.h>

const int IN1 = 13;
const int IN2 = 12;
const int EN1 = 3;
int angle = 0;


void setup() {
  pinMode(IN1, OUTPUT); 
  pinMode(IN2, OUTPUT);
  pinMode(EN1, OUTPUT);
}

void loop() {
  digitalWrite(IN1, 1);
  digitalWrite(IN2, 1);
  analogWrite(3, 53);
}
