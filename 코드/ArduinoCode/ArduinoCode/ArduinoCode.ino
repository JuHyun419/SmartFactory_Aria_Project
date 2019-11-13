// 일반 입출력 데이터 핀을 RX(수신), TX(송신)핀으로 동작할 수 있게 해주는 라이브러리
#include <SoftwareSerial.h>
#include <Servo.h>  // Servo 라이브러리 추가

// const = 상수, "읽기 전용"으로 만드는 변수 한정자
const int SERVO_PWM1 = 6;
const int SERVO_PWM2 = 5;
const int IN1 = 13;
const int IN2 = 12;
const int EN1 = 11; // 모터의 속도 결정하는 핀번호
const int rx = 7;
const int tx = 8;

String rx_data = "";
int angle = 0;

Servo servo1;
Servo servo2;
SoftwareSerial swSerial(rx, tx);

void setup() 
{ 
  // 핀의 입출력 모드 설정
  pinMode(IN1, OUTPUT); // 13번
  pinMode(IN2, OUTPUT); // 12번
  pinMode(EN1, OUTPUT); // 11번

  // 서보모터 설정
  servo1.attach(SERVO_PWM1);  // 6번
  servo2.attach(SERVO_PWM2);  // 5번
  
  digitalWrite(IN1, 0); // 13번
  digitalWrite(IN2, 0); // 12번
  analogWrite(EN1, 0);  // 11번

  // 서보모터 각도 설정(0 ~ 180도)
  servo1.write(180);
  servo2.write(90);
  
  Serial.begin(9600);
  swSerial.begin(9600);
}

void loop() 
{  
   // 데이터가 들어있는지 확인
   if(swSerial.available())
   {
      rx_data = Rec_data();
      
      if (rx_data == "go")
      {
          Serial.println("go");
          dc_op();
      }
      
      else if(rx_data == "stop")
      {
         Serial.println("stop");
         dc_st();
      }
      
      
      if(rx_data == "rgrab")
      {
        Serial.println("rgrab");
        Grab_Regular_object();
        delay(100);
        swSerial.write("complete\n");  
      }

      else if(rx_data == "fgrab")
      {
        Serial.println("fgrab");
        swSerial.write("complete\n");  
      }
   }
}

// 공백까지 data 반환하는 함수
String Rec_data()
{
  String data = "";
  data = swSerial.readStringUntil('\n');
  return data;
}

// 로봇팔 회전모터
void open_teol()
{
  for(angle = 0; angle <= 180; angle++) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}

// 로봇팔 회전모터
void close_teol()
{
  for(angle = 180; angle >= 0; angle--) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}

void Grab_Regular_object()
{
  close_teol();
  delay(100);
  servo1.write(0);
  delay(100);
  open_teol();
  delay(100);  
  servo1.write(90);
}

void Grab_Inferior_object()
{
  close_teol();
  delay(100);
  servo1.write(180);
  delay(100);
  open_teol();
  delay(100);  
  servo1.write(90);
}

// 
void dc_op()
{
  digitalWrite(IN1, 0); // 13
  digitalWrite(IN2, 1); // 12
  analogWrite(EN1, 53); // 11, 아날로그 값을 핀에 출력
}

void dc_st()
{
  digitalWrite(IN1, 0);
  digitalWrite(IN2, 0);
  analogWrite(EN1, 0);
}
