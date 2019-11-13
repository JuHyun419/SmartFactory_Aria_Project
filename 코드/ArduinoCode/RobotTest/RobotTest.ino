// 일반 입출력 데이터 핀을 RX(수신), TX(송신)핀으로 동작할 수 있게 해주는 라이브러리
#include <SoftwareSerial.h>
#include <Servo.h>  // Servo 라이브러리 추가

// const = 상수, "읽기 전용"으로 만드는 변수 한정자
const int SERVO_PWM1 = 6;
const int SERVO_PWM2 = 5;
const int IN1 = 13;
const int IN2 = 12;
const int EN1 = 11; // 모터의 속도 결정하는 핀번호
const int rx = 2;
const int tx = 3;

String rx_data = "";
int angle = 0;

Servo servo1;
Servo servo2;
SoftwareSerial swSerial(rx, tx);


void setup() {
  
  
  pinMode(IN1, OUTPUT); // 13번
  pinMode(IN2, OUTPUT); // 12번
  pinMode(EN1, OUTPUT); // 11번

  // 서보모터 설정
  servo1.attach(SERVO_PWM1);  // 6번
  servo2.attach(SERVO_PWM2);  // 5번


  // 서보모터 각도 설정(0 ~ 180도)
  servo1.write(0);
  servo2.write(90);

  Serial.begin(9600);
  swSerial.begin(9600);
  
  
}

void loop() {

  
}


void open_teol()
{
  for(angle = 0; angle <= 180; angle++) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}


void close_teol()
{
  for(angle = 180; angle >= 0; angle--) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}
