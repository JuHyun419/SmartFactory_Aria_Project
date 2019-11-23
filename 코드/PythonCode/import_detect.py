import cv2 as cv
import numpy as np  # 배열을 처리하는데 필요한 라이브러리
from multiprocessing import Queue, Process
from pyzbar import pyzbar   # 바코드, QR코드 읽는 라이브러리
from AriaMethod import *    # AriaMethod.py 파일 불러옴

## 서버IP, Port 정의
#ServerIP = "220.69.249.231"
ServerIP = "220.69.249.226"
Port = 4000

CAM_ID = 0
CAM_WIDTH = 352  #480
CAM_HEIGHT = 288 #320

signal = 'N'
data = ""
flag = 1

# blue 영역의 from ~ to
lower_blue = np.array([90, 171, 149])
upper_blue = np.array([120,255,255])

# red 영역의 from ~ to
lower_red1 = np.array([0, 14, 220]) 
upper_red1 = np.array([9, 255, 255])

lower_red2 = np.array([0, 97, 214]) 
upper_red2 = np.array([14, 255, 255])

# 카메라 실행
def open_cam(camera = CAM_ID):
    
    # 동영상 관리 함수
    cap = cv.VideoCapture(camera)   
    
    if cap.isOpened():  
        # 화면 크기 설정
        cap.set(cv.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)
        return cap
    else:
        print("camera open failed \n")

def cam_streaming(cap):
    ret, frame = cap.read()
    
    if ret == True:
        return frame
    
    else:
        print("camera read error \n")
        
# 이미지 필터링
# HSV - 이미지 처리에서 가장 많이 사용되는 형태의 Color 모델
#       하나의 모델에서 색, 채도, 명도를 모두 알 수 있음 
def image_filter(frame):
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # BGR -> HSV로 변환
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # BGR -> HSV로 변환

    # 이미지에서 blue, red 영역
    mask_blue = cv.inRange(hsv_blue, lower_blue, upper_blue)
    mask_red1 = cv.inRange(hsv_red, lower_red1, upper_red1)
    mask_red2 = cv.inRange(hsv_red, lower_red2, upper_red2)
    mask_red = cv.bitwise_or( mask_red1, mask_red2)

    # 이미지 형태전환(?)
    # erode - 침식
    #         전경이 되는 이미지의 경계부분을 침식시켜 배경 이미지로 전환
    #         반복할수록 대상 이미지는 더더욱 가늘어지게 됨
    # dilate - 팽창(침식과 반대)
    
    # mask_blue : erosion을 수행할 원본 이미지
    # None : erosion을 위한 커널(None)
    # iterations : Erosion 반복 횟수
    erode_blue_image = cv.erode(mask_blue, None, iterations = 2)
    dilate_blue_image = cv.dilate(mask_blue, None, iterations = 2)
    
    erode_red_image = cv.erode(mask_red, None, iterations = 2)
    dilate_red_image = cv.dilate(mask_red, None, iterations = 2)
    
    return dilate_blue_image, dilate_red_image 

# 제품 찾는 함수
def detect_goods(filter_blue_image, filter_red_image, frame):

    # Contour - 같은 값을 가진 곳을 연결한 선
    contours_blue = cv.findContours(filter_blue_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    contours_red = cv.findContours(filter_red_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    # 파랑색 제품
    if len(contours_blue) > 0:
        c = max(contours_blue, key=cv.contourArea)
        signal = 'P'    
    
    # 빨간색 제품
    elif len(contours_red) > 0:
        c = max(contours_red, key=cv.contourArea)
        signal = 'F'
    
    # 제품이 없을때
    else:
        signal = 'N'
        #print("no goods ! signal: N \n\n")
        x = 9999 
        y = 9999
        data = ""
        return x, signal, data, frame
 
    ((x, y), radius) = cv.minEnclosingCircle(c) 
    x = int(x)
    y = int(y)
      
    if int(radius) > 15:
        # print("detect_goods@@@@@")
        (data, frame) = read_barcode(frame)
        #print("QRCODE: " + data + " signal: " + signal + "\n\n")
        cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv.circle(frame, (int(x), int(y)), 5, (0, 255, 255), -1)
        cv.putText(frame, str(x)+' , '+str(y), (x, y + 40), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 255), 2)
        return x, signal, data, frame
    
    else:
        x = -1
        y = -1
        data = ""
        return x, signal, data, frame

# 바코드 찾고 읽는 함수
def read_barcode(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 전역변수 설정
    global flag

    # 이미지에서 바코드를 찾고 각 바코드를 디코드한다.
    decoded = pyzbar.decode(gray)   
    barcode_data = ""
    
    if len(decoded) > 0:

        # 검출한 바코드를 위한 루프
        for d in decoded: 

            # 바코드의 영역을 추출하고 영역 그리기
            # 이미지의 바코드 주변에 박스를 그림
            x, y, w, h = d.rect

            # 바코드 데이터는 바이트 객체이므로 이미지에 그리려면 문자열로 변환해야함
            barcode_data = d.data.decode("utf-8")   # .decode("utf-8") : byte -> 문자열 변환 
            barcode_type = d.type

            # 바코드 데이터와 타입을 이미지에 그림
            text = '%s (%s)' % (barcode_data, barcode_type)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv.LINE_AA)

            # ## QR코드의 데이터를 한번만 전송하기 위한 조건문
            # if(flag == 1):
            #     # Server에 접속
            #     clientSock = connToServer(ServerIP, Port)
            #     print("---------- barcode_data ----------")
            #     print(barcode_data)

            #     # Aria 프로토콜 정의
            #     # {{product_number, model_name, Line}}
            #     aria_barcode_data = "{{" + barcode_data + "}}"

            #     # Server에 QR코드 전송
            #     # encode() : 문자열 -> Byte 변환2
            #     clientSock.send(aria_barcode_data.encode('utf-8'))
            #     print("----------------------------------")
            #     flag -= 1   # 전역변수 flag값을 감소시켜 다음에 함수가 실행되도 if문 실행 X
            return barcode_data, frame
    else:
        return barcode_data, frame    

def cam(cap):
    frame = cam_streaming(cap)
    frame = cv.GaussianBlur(frame, (1, 1), 0)
    (filter_blue_image, filter_red_image) = image_filter(frame)
    x, signal, data, frame = detect_goods(filter_blue_image, filter_red_image, frame)

    # rectangle() : 사각형 그려주는 함수
    cv.rectangle(frame, (50, 0), (302, 288), (0, 0, 255), 2)

    # imshow() : 이미지를 사이즈에 맞게 보여줌
    cv.imshow('frame', frame)
    cv.imshow('filter_blue_mask', filter_blue_image)
    cv.imshow('filter_red_mask', filter_red_image)
    return x, signal, data 