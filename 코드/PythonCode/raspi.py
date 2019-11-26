import serial   # 아두이노 통신 라이브러리
from time import *  
from multiprocessing import Queue, Process
from import_detect import * # import_detect.py 파일 불러옴
import Adafruit_DHT         # 온습도 관련 라이브러리
from AriaMethod import *    # AriaMethod.py 파일 불러옴
from threading import Thread    # 쓰레드 관련 라이브러리
import time as time1        # 타임 관련 라이브러리


## 서버IP, Port 정의
#ServerIP = "220.69.249.231"
ServerIP = "220.69.249.226"
Port = 4000

CompleteProduct = 0 # 정상품 카운트 할 변수
BAUDRATE = 9600
time_flag = 0
last_time = 0

time_flag2 = 0
last_time2 = 0

# SystemBytePlus() 함수에서 사용될 문자열, 리스트
SystemByteResult = ""
SystemByteResult2 = ""
SystemByte = [0, 0, 0, 0, 1]

sensor = Adafruit_DHT.DHT11
pin = '4'

## 00001 부터 1씩 증가하는 함수
def SystemBytePlus():
    SystemByte[4] +=1   # 일의자리 1씩 증가
    if(SystemByte[4] == 10):    # 일의자리가 10이 됬을때
        SystemByte[3] += 1      # 십의자리 +1
        SystemByte[4] = 0       # 일의자리 초기화
    
    if(SystemByte[3] == 10):    # 십의자리가 10이 됬을때
        SystemByte[2] += 1      # 백의자리 +1
        SystemByte[3] = 0       # 십의자리 초기화
    
    if(SystemByte[2] == 10):    # 백의자리가 10이 됬을때
        SystemByte[1] += 1      # 천의자리 +1
        SystemByte[2] = 0       # 백의자리 초기화

    if(SystemByte[1] == 10):    # 천의자리가 10이 됬을때
        SystemByte[0] += 1      # 만의자리 +1
        SystemByte[1] = 0       # 천의자리 초기화
    
    # 문자열 합치기
    SystemByteResult = str(SystemByte[0]) + str(SystemByte[1]) + str(SystemByte[2]) + str(SystemByte[3]) + str(SystemByte[4])
    return SystemByteResult

# ## 온, 습도 리턴 함수
# def humanity_temp():
#     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
#     # 온, 습도 값이 존재할때
#     if humidity is not None and temperature is not None:
#         return int(temperature), int(humidity)  # 온습도 값 리턴

#     # 온, 습도 값이 존재하지 않을때
#     else:
#         #print('Failed to get reading. Try again!')
#         temperature = 0 
#         humidity = 0 
#         return temperature, humidity   # 온습도 0으로 초기화 후 리턴

## 시리얼 객체 생성(open) - 아두이노 통신
def serial_open():
    ser = serial.Serial('/dev/ttyAMA0', baudrate = BAUDRATE)
    return ser

## 아두이노에게 전송 방식
def command_arduino(ser, i):
    command = ["go\n", "stop\n", "rgrab\n", "fgrab\n"]
    
    command[i] = command[i].encode('utf-8')
    ser.write(command[i])

## 아두이노에서 데이터 받는 함수
def receive_arduino(ser, q):
    if ser.readable():
        data = ser.readline()

        # decode() : 바이트로 들어온 데이터 해결
        data = str(data[:-1].decode())  
        q.put(data)

## 온습도 출력
# def get_H_T():
#     global time_flag
#     global last_time

#     if time_flag == 0:
#         last_time = time()
#         time_flag = 1

#     # 10초 간격 온습도 출력
#     if time() - last_time >= 5:
#         temp, hum = humanity_temp()
#         time_flag = 0
#         now = time1.localtime()
#         print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
#         print('Temp={0}*C  Humidity={1}%'.format(temp, hum))

def image_process(cap, ser, q, state_flag, state_list):

    goods_x, signal, barcode = cam(cap)
    global CompleteProduct

    # 받은 신호가 P(블루) 일때, 카메라가 블루 제품을 확인하고 컨베이어 벨트를 멈추는 범위
    if signal == 'P' and (goods_x >= 5 and goods_x <= 260): 

        if state_flag == "SEND_STOP":   # 상태가 STOP 일때

            # --------------------------------------------------------------
            command_arduino(ser, 1)
            state_flag = "SEND_GRAB"    # 상태 GRAB

            # 온습도 받아오는 함수
            hum, temp = Adafruit_DHT.read_retry(sensor, pin)

            # 온습도값 int로 형변환
            temp = int(temp)
            hum = int(hum)

            if(temp != 0 and hum != 0):
                # 한번 전송될때마다 1씩 증가(00001, 00002, 00003, ...) 
                SystemByteResult2 = SystemBytePlus()

                # Server로 temp, hum 전송
                Send_s6f11_TempHumid(ServerIP, Port, SystemByteResult2, temp, hum)

                # 현재 시간, 온습도 출력 로그
                now = time1.localtime()
                print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                print("온도 : %d, 습도 : %d 값이 MES Server로 전송되었습니다." % (temp, hum))
            else:
                print("온도, 습도값이 비정상적입니다.")

            CompleteProduct += 1    # 파랑색 제품 1개 추가

            # 생산개수 / 총개수(Server로 전송 방식)
            Prod_Percent_Blue = str(CompleteProduct) + "/" + str(Prod_count)

            # 명령 보낼때마다 1씩 증가(00001, 00002, 00003, ...)
            SystemByteResult = SystemBytePlus()

            # Blue(정상) 제품 생산 완료시 서버에게 전송하는 데이터
            Send_s6f11_Complete_Blue(ServerIP, Port, SystemByteResult, "10", Model_name, CompleteProduct)


        if state_flag == "SEND_GRAB"  and len(barcode) > 5:
            sleep(0.01)
            command_arduino(ser, 2)
            state_flag = "WAIT"
            
    # 받은 신호가 F(레드) 일때, 카메라가 레드 제품을 확인하고 컨베이어 벨트를 멈추는 범위
    elif signal == 'F' and (goods_x >= 5 and goods_x <= 260):
        
        if state_flag == "SEND_STOP":
            command_arduino(ser, 1)
            state_flag = "SEND_GRAB"

            # 온습도 받아오는 함수
            hum, temp = Adafruit_DHT.read_retry(sensor, pin)

            # 온습도값 int로 형변환
            temp = int(temp)
            hum = int(hum)

            if(temp != 0 and hum != 0):
                # 한번 전송될때마다 1씩 증가(00001, 00002, 00003, ...) 
                SystemByteResult2 = SystemBytePlus()

                # Server로 temp, hum 전송
                Send_s6f11_TempHumid(ServerIP, Port, SystemByteResult2, temp, hum)

                # 현재 시간, 온습도 출력 로그
                now = time1.localtime()
                print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                print("온도 : %d, 습도 : %d 값이 MES Server로 전송되었습니다." % (temp, hum))
            else:
                print("온도, 습도값이 비정상적입니다.")

            CompleteProduct += 1     # 완성개수

            # 생산개수 / 총개수
            Prod_Percent_Blue = str(CompleteProduct) + "/" + str(Prod_count)
            
            # 명령 보낼때마다 1씩 증가
            SystemByteResult = SystemBytePlus()
            Send_s6f11_Complete_Red(ServerIP, Port, SystemByteResult, "10", Model_name, CompleteProduct)


        if state_flag == "SEND_GRAB"  and len(barcode) > 5:
            sleep(0.01)
            command_arduino(ser, 3)
            state_flag = "WAIT"
            
    else:
        if q.empty() == False and signal == 'N':
            rx_data = q.get()
            print(rx_data)
            if rx_data == "complete":
                command_arduino(ser, 0)
                state_flag = "SEND_STOP"
    return state_flag


def main_process(ser, q):
    state_list = ["WAIT", "SEND_STOP", "SEND_GRAB" ]
    cap = open_cam()    # 카메라 open
    command_arduino(ser, 0)
    state_flag = state_list[1]
    q.put("start")
    
    sleep(1)
    
    while True:
        state_flag = image_process(cap, ser, q, state_flag, state_list)    
        if cv.waitKey(1) & 0xFF == 27:
            break 
    cap.release()
    cv.destroyAllWindows()  

def serve_process(ser, q):
    while True:
        receive_arduino(ser, q)

# -------------------------- 주석처리 4시 54분-----------------------
# ## 온습도 받는 process
# def temp_huminity_process(q):
    
#     print("=====================")
#     print("temp_huminity_process")
#     print("=====================")

#     factory_state = ""
#     temp_state = 1

#     while True:
#         if q.empty() == False and temp_state == 1:
#             factory_state = q.get()
#             temp_state = 2
        
#         if factory_state == "start" and temp_state == 2:
#             get_H_T()

try:
    if __name__ == "__main__":
        print("start \n")
        
        # ----------------------------------------------------------
        while True:
            clientSock = connToServer(ServerIP, Port)   # Server에 접속
            clientSock.send("value = ?".encode('utf-8'))    # encode() - 문자열을 byte로 변환
            data = clientSock.recv(1024)    # 서버로부터 데이터 받음
            print("MES Server로부터 수신 데이터 대기중...")   # decode() - byte를 문자열로 변환
            recvData = data.decode('utf-8') # Server로 부터 받은 byte를 문자열로 변환
            ser = serial_open()
            command_arduino(ser, 1)

            # Server로 부터 받은 데이터가 false가 아닐때,
            # 실직적으로 공장 시작되는 시점
            if recvData != 'false':
                # Server로 부터 받은 데이터중 필요한 데이터를 뽑아냄
                # Model_name  : 아리아크림빵,
                # Prod_count  : 상품 개수
                # Color       : 상품 색상
                Model_name, Prod_count, Color = Receive_s2f41(recvData)
                print("------------------------------------------")
                now = time1.localtime()
                print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                time1.sleep(1)
                print("MES Server로 부터 작업지시 명령을 받았습니다.")
                time1.sleep(1)
                print("------------------------------------------")

                # 명령 보낼때마다 1씩 증가
                SystemByteResult = SystemBytePlus()

                # Server에게 작업 지시에 대한 응답 전송
                Send_s2f42(ServerIP, Port, SystemByteResult)
                print("제품이름 : " + Model_name)
                print("제품수량 : " + Prod_count)
                print("제품색상 : " + Color)
                print()

                print("3초뒤 Aria 공정이 작동됩니다.")
                time1.sleep(3)
                command_arduino(ser, 0)
                break
            time1.sleep(2)  # 2초 딜레이
        # ----------------------------------------------------------

        q = Queue()
        ser = serial_open()
        p1 = Process(target = main_process, args = (ser,q))
        p2 = Process(target = serve_process, args = (ser,q))
        #p3 = Process(target = temp_huminity_process, args = (q, ))

        p1.start()
        p2.start()
        #p3.start()
except KeyboardInterrupt:
    print("exit() \n")
    p1.join()
    p2.join()
    #p3.join()
