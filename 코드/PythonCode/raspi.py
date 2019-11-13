import serial   # 아두이노 통신 라이브러리
from time import *  
from multiprocessing import Queue, Process
from import_detect import * # import_detect.py 파일 불러옴
import Adafruit_DHT         # 온습도 관련 라이브러리
from AriaMethod import *    # AriaMethod.py 파일 불러옴


BAUDRATE = 9600
time_flag = 0
last_time = 0

# SystemBytePlus() 함수에서 사용될 문자열, 리스트
SystemByteResult = ""
SystemByte = [0, 0, 0, 0, 0]


sensor = Adafruit_DHT.DHT11
pin = '4'


# 00001 부터 1씩 증가하는 함수
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

# 온, 습도 리턴 함수
def humanity_temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # 온, 습도 값이 존재할때
    if humidity is not None and temperature is not None:
        return int(temperature), int(humidity)  # 온습도 값 리턴

    # 온, 습도 값이 존재하지 않을때
    else:
        #print('Failed to get reading. Try again!')
        temperature = 0 
        humidity = 0 
        return temperature, humidity   # 온습도 0으로 초기화 후 리턴
    
# 시리얼 객체 생성(open)
def serial_open():
    ser = serial.Serial('/dev/ttyAMA0', baudrate = BAUDRATE)
    return ser

# 아두이노에게 전송 방식
def command_arduino(ser, i):
    command = ["go\n", "stop\n", "rgrab\n", "fgrab\n"]
    
    command[i] = command[i].encode('utf-8')
    ser.write(command[i])

# 아두이노에서 데이터 받는 함수
def receive_arduino(ser, q):
    if ser.readable():
        data = ser.readline()

        # decode() : 바이트로 들어온 데이터 해결
        data = str(data[:-1].decode())  
        q.put(data)



# 온습도 출력
def get_H_T():
    
    global time_flag
    global last_time
    
    if time_flag == 0:
        last_time = time()
        time_flag = 1
    
    # 10초 간격 온습도 출력
    if time() - last_time >= 3:
        temp, hum = humanity_temp()
        time_flag = 0
        print('Temp={0}*C  Humidity={1}%'.format(temp, hum))
        SystemByteResult = SystemBytePlus()
        Send_s6f11_TempHumid(SystemByteResult, temp, hum)
   
#def image_process(cap, ser, q, state_flag = 1):
    
def main_process(ser, q):

    cap = open_cam()
    command_arduino(ser, 0)
    state_flag = 1
    sleep(1)
    
    while True:
        goods_x, signal, barcode = cam(cap)
        
        if signal == 'P' and (goods_x >= 50 and goods_x <= 302):
            if state_flag == 1:
                command_arduino(ser, 1)
                state_flag = 2
            if len(barcode) > 5 and state_flag == 2:
                sleep(0.01)
                command_arduino(ser, 2)
                state_flag = 0
                
        elif signal == 'F' and (goods_x >= 50 and goods_x <= 302):
            if state_flag == 1:
                command_arduino(ser, 1)
                state_flag = 2
            if len(barcode) > 5 and state_flag == 2:
                sleep(0.01)
                
        else:
            if q.empty() == False and signal == 'N':
                rx_data = q.get()
                print(rx_data)
                if rx_data == "complete":
                    command_arduino(ser, 0)
                    state_flag = 1
                    
        if cv.waitKey(1) & 0xFF == 27:
            break 
        
        get_H_T()
            
    cap.release()
    cv.destroyAllWindows()  

def serve_process(ser, q):
    while True:
        receive_arduino(ser, q)
        
        
try:
    if __name__ == "__main__":
        SystemByte = [0, 0, 0, 0, 0]
        print("start \n")
        q = Queue()
        ser = serial_open()
        p1 = Process(target = main_process, args = (ser,q))
        p2 = Process(target = serve_process, args = (ser,q))
        p1.start()
        p2.start()

except KeyboardInterrupt:
    print("exit() \n")
    p1.join()
    p2.join()

