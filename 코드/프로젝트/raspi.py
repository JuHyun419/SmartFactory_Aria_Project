import serial   # 아두이노 통신 라이브러리
from time import *  
from multiprocessing import Queue, Process
from import_detect import *
import Adafruit_DHT # 온습도 라이브러리
from socket import *
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump    # XML 모듈
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import xml.etree.ElementTree as ET

BAUDRATE = 9600
time_flag = 0
last_time = 0

sensor = Adafruit_DHT.DHT11
pin = '4'

clientSock = socket(AF_INET, SOCK_STREAM)
#clientSock.connect(('220.69.249.226', 4000))

# XML 형식의 온습도 문자열
def getTempHumid(temp, humid):
    xmlStr ='''
        <SECS2_XML_MESSAGE>
            <HEAD>
                <SystemByte>00001</SystemByte>
                <CMD>3</CMD>
                <Stream>2</Stream>
                <Function>42</Function>
            </HEAD>
            <BODY>
                <HCACK>0</HCACK>
                <TEMP>'''  + temp  + '''</TEMP>    
                <HUMID>''' + humid + '''</HUMID>
            </BODY>
        </SECS2_XML_MESSAGE>
        '''
    return xmlStr

# 온습도 받아오는 함수
def humanity_temp():

    # 온습도 라이브러리
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # 온습도 값이 존재할 때 -> 온습도값 리턴
    if humidity is not None and temperature is not None:
        return int(temperature), int(humidity)

    # 온습도 값이 존재하지 않을 때
    else:
        #print('Failed to get reading. Try again!')
        temperature = 0 
        humidity = 0 
        return temperature, humidity   
    
# 시리얼 객체 생성(ser) - 아두이노 통신
def serial_open():
    ser = serial.Serial('/dev/ttyAMA0', baudrate = BAUDRATE)
    return ser

# 아두이노에게 데이터 전송
def command_arduino(ser, i):
    command = ["go\n", "stop\n", "rgrab\n", "fgrab\n"]
    
    command[i] = command[i].encode('utf-8')
    ser.write(command[i])

# 아두이노로 부터 데이터 받는 함수
def receive_arduino(ser, q):
    if ser.readable():
        data = ser.readline()

        # decode() : 바이트로 들어온 데이터 해결
        data = str(data[:-1].decode())  
        q.put(data)

# 온습도 출력(10초기준)
def get_H_T():
    global time_flag
    global last_time
    
    if time_flag == 0:
        last_time = time()
        time_flag = 1
    
    if time() - last_time >= 10:

        # 온습도 받아오는 함수
        temp, humid = humanity_temp()   
        time_flag = 0

        # 서버에 전송할 XML 형식의 온습도 문자열
        SendTempHumid = getTempHumid(temp, humid)
        clientSock.send(SendTempHumid.encode('utf-8'))  # 서버로 전송
        print('Temp={0}*C  Humidity={1}%'.format(temp, humid))

# 이미지 처리(카메라)
def image_process(cap, ser, q, state_flag, state_list):
    goods_x, signal, barcode = cam(cap)

    # 정상, 비정상 저장할 변수, 정상 - 1, 비정상 - 2
    global Color    
  
    # 파랑색 제품(정상품) - 1
    if signal == 'P' and (goods_x >= 60 and goods_x <= 272):
        Color = 1
        if state_flag == "SEND_STOP":
            command_arduino(ser, 1)
            state_flag = "SEND_GRAB"
            print("P, SEND_STOP")

        if state_flag == "SEND_GRAB"  and len(barcode) > 5:
            sleep(0.01)
            command_arduino(ser, 2)
            state_flag = "WAIT"
            print("P, SEND_GRAB")
            
    # 빨강색 제품(불량품) - 2
    elif signal == 'F' and (goods_x >= 60 and goods_x <= 272):
        Color = 2
        if state_flag == "SEND_STOP":
            command_arduino(ser, 1)
            state_flag = "SEND_GRAB"

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

    cap = open_cam()
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
        
def temp_huminity_process(q):
    factory_state = ""
    temp_state = 1
    
    while True:
        if q.empty() == False and temp_state == 1:
            factory_state = q.get()
            temp_state = 2
        
        if factory_state == "start" and temp_state == 2:
            get_H_T()
try:
    if __name__ == "__main__":
        print("start \n")
        q = Queue()
        ser = serial_open()
        p1 = Process(target = main_process, args = (ser,q))
        p2 = Process(target = serve_process, args = (ser,q))
        p3 = Process(target = temp_huminity_process, args = (q, ))
        p1.start()
        p2.start()
        p3.start()
        print("ggggg")
        
except KeyboardInterrupt:
    print("exit() \n")
    p1.join()
    p2.join()
    p3.join()