#include <SoftwareSerial.h> // 시리얼 통신 라이브러리
#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

const int GRAB_UNDER_SERVO = 5;
const int GRAB_UPPER_SERVO = 6;
const int BASKET_LEFT_SERVO = 10;
const int BASKET_RIGHT_SERVO = 9;

// 컨베이어 벨트
const int IN1 = 12;
const int IN2 = 13;
const int EN1 = 3;  

// 피니언 렉
const int IN3 = 2;
const int IN4 = 4;
const int EN2 = 11;

const int rx = 8;
const int tx = 7;
SoftwareSerial swSerial(rx, tx);

String rx_data = "";
int angle = 0;
int red_count = 0, blue_count = 0;

void setup() 
{
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(EN1, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(EN2, OUTPUT);

  servo1.attach(GRAB_UNDER_SERVO);  // 로봇팔 회전 모터, 5번
  servo2.attach(GRAB_UPPER_SERVO);  // 로봇팔, 6번
  servo3.attach(BASKET_LEFT_SERVO); // 왼쪽 바구니, 10번
  servo4.attach(BASKET_RIGHT_SERVO);  // 오른쪽 바구니, 9번

  // 컨베이어
  digitalWrite(IN1, 0); // 12번
  digitalWrite(IN2, 0); // 13번
  analogWrite(EN1, 0);  // 3번

  // 피니언 랙
  digitalWrite(IN3, 0); // 2번
  digitalWrite(IN4, 0); // 4번
  analogWrite(EN2, 0);  // 11번

  // 각 모터 초기화 값
  servo1.write(90);   // 로봇팔 회전해주는 모터 - 초기값 
  servo2.write(180);  // 로봇팔 - 0 : 접은거, 180 : 펼친거
  servo3.write(180);  // 왼쪽바구니 - 0 : 엎음, 180 : 초기값
  servo4.write(0);    // 오른쪽 바구니 - 0 : 초기값, 180 : 엎음    
  
  Serial.begin(9600);
  swSerial.begin(9600);
}

void loop() 
{  
   // 파이로부터 받은 데이터가 있을때
   if(swSerial.available())
   {
      rx_data = Rec_data();
      
      if (rx_data == "go")
      {
          Serial.println("go");
          conveyer_dc_op();
      }
       
      else if(rx_data == "stop")
      {
         Serial.println("stop");
         conveyer_dc_st();
      }
      
      else if(rx_data == "rgrab")
      {
        Serial.println("rgrab");
        blue_count ++;
        Grab_Regular_object();
        delay(1000);
        
        if(blue_count == 1)
        {
          Input_Left_Basket();
        }
        blue_count = 0;
        swSerial.write("complete\n");  
      }

      else if(rx_data == "fgrab")
      {
        Serial.println("fgrab");
        red_count ++;
        Grab_Inferior_object();
        delay(1000);
        
        if(red_count == 1)
        {
          Input_Right_Basket();
        }
        red_count = 0;
        swSerial.write("complete\n");    
      }
   }
}

// 데이터 읽어오는 함수
String Rec_data()
{
  String data = "";
  data = swSerial.readStringUntil('\n');
  return data;
}

// 좌측 바구니 관련 함수
void left_basket_op()
{
  // 좌측 바구니 비우기(100도 회전)
  for(angle = 180; angle >= 80; angle--) 
  { 
    servo3.write(angle); 
    delay(25);
  } 

  delay(1000);

  // 좌측 바구니를 비운 상태에서 원위치
  for(angle = 80; angle <= 180; angle++) 
  { 
    servo3.write(angle); 
    delay(25); 
  }
}

// 우측 바구니 관련 함수
void right_basket_op()
{
  // 우측 바구니 비우기(100도 회전)
  for(angle = 0; angle <= 100; angle++) 
  { 
    servo4.write(angle); 
    delay(25);
  } 

  delay(1000);

  // 우측 바구니를 비운 상태에서 원위치
  for(angle = 100; angle >= 0; angle--) 
  { 
    servo4.write(angle); 
    delay(15); 
  }
}

// 로봇팔 접은상태 -> 펴기(초기 상태로)
void open_teol()
{
  // 로봇팔 초기값 - 180도
  for(angle = 0; angle <= 180; angle++) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}

// 로봇팔 편상태(초기 상태) -> 접은상태
void close_teol()
{
  // 로봇팔 초기 - 180도
  for(angle = 180; angle >= 0; angle--) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}

// 정상 잡는 함수
void Grab_Regular_object()
{
  close_teol(); // 로봇팔 접기
  delay(100);
  servo1.write(0);  // 로봇팔 회전(왼쪽)
  delay(100);
  open_teol();  // 로봇팔 펴기
  delay(100);  
  servo1.write(90); // 로봇팔 회전(원위치)
}

// 불량 잡는 함수(정상 잡는 함수와 반대)
void Grab_Inferior_object()
{
  close_teol(); // 로봇팔 접기
  delay(100);
  servo1.write(180);  // 로봇팔 회전(오른쪽)
  delay(100);
  open_teol();  // 로봇팔 펴기
  delay(100);  
  servo1.write(90); // 로봇팔 회전(원위치)
}

// 우측 바구니 담는 함수
void Input_Right_Basket()
{
  rack_forward(); // 피니언을 박스담는 쪽으로 움직이는 함수
  delay(100);
  rack_stop();    // 피니언 정지
  delay(100);
  right_basket_op();  // 우측 바구니 비운 후 원위치
  delay(100); 
  rack_backward();  // 피니언 컨베이어 벨트로 원위치
  delay(100);
  rack_stop();    // 피니언 정지
}

// 좌측 바구니 담는 함수
void Input_Left_Basket()
{
  rack_forward(); // 피니언을 박스담는 쪽으로 움직이는 함수
  delay(100);
  rack_stop();    // 피니언 정지
  delay(100);
  left_basket_op(); // 좌측 바구니 비운 후 원위치
  delay(100); 
  rack_backward();  // 피니언 컨베이어 벨트로 원위치
  delay(100);
  rack_stop();    // 피니언 정지
}

// 피니언 움직이는 함수(박스 쪽으로)
void rack_forward()
{
  digitalWrite(IN3, 1); // 2번
  digitalWrite(IN4, 0); // 4번
  analogWrite(EN2, 35); // 11번
  delay(4800);
}

// 피니언 움직이는 함수(컨베이어 벨트쪽으로)
void rack_backward()
{
  digitalWrite(IN3, 0); // 2번
  digitalWrite(IN4, 1); // 4번
  analogWrite(EN2, 35); // 11번
  delay(4600);
}

// 피니언 정지 함수
void rack_stop()
{
  digitalWrite(IN3, 0);
  digitalWrite(IN4, 0);
  analogWrite(EN2, 0);
}

// 컨베이어벨트 동작 함수(0, 1 = 정방향, 53 = 속도)
void conveyer_dc_op()
{
  digitalWrite(IN1, 0); // 12번
  digitalWrite(IN2, 1); // 13번
  analogWrite(EN1, 51); // 3번
}

// 컨베이어벨트 정지 함수
void conveyer_dc_st()
{
  digitalWrite(IN1, 0); // 12번
  digitalWrite(IN2, 0); // 13번
  analogWrite(EN1, 0);  // 3번
}
