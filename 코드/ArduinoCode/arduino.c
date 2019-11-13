// �Ϲ� ����� ������ ���� RX(����), TX(�۽�)������ ������ �� �ְ� ���ִ� ���̺귯�� 
#include <SoftwareSerial.h>	
#include <Servo.h>	// Servo ���̺귯�� �߰� 

// const = ���, "�б� ����"���� ����� ���� ������ 
const int SERVO_PWM1 = 6;
const int SERVO_PWM2 = 5;
const int IN1 = 13;
const int IN2 = 12;
const int EN1 = 11;	// ������ �ӵ� ���� 
const int rx = 2;
const int tx = 3;

String rx_data = "";
int angle = 0;

Servo servo1;
Servo servo2;
SoftwareSerial swSerial(rx, tx);

void setup() 
{
  // ���� ����� ��� ���� 
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(EN1, OUTPUT);

  // �������͸� ��� ������ ��Ʈ������ �����ϴ� �Լ� 
  servo1.attach(SERVO_PWM1);	// 6�� 
  servo2.attach(SERVO_PWM2);	// 5�� 

  // HIGH �Ǵ� low �� ��� 
  digitalWrite(IN1, 0);
  digitalWrite(IN2, 0);
  analogWrite(EN1, 0);

  // ���������� ���� ����(0~180)
  servo1.write(90);
  servo2.write(180);
  
  Serial.begin(9600);
  swSerial.begin(9600);
}

void loop() 
{  
   // �����Ͱ� ���Դ��� Ȯ�� 
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

// ������� data ��ȯ�ϴ� �Լ� 
String Rec_data()
{
  String data = "";
  data = swSerial.readStringUntil('\n');
  return data;
    
}

// �κ��� ���� 
void open_teol()
{
  for(angle = 0; angle <= 180; angle++) 
  { 
    servo2.write(angle); 
    delay(25); 
  } 
}

// �κ��� ��ħ 
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

// ���� ���� �Լ� 
void dc_op()
{
  digitalWrite(IN1, 0);
  digitalWrite(IN2, 1);
  analogWrite(EN1, 53);
}

// ���� ���� �Լ� 
void dc_st()
{
  digitalWrite(IN1, 0);
  digitalWrite(IN2, 0);
  analogWrite(EN1, 0);
}
