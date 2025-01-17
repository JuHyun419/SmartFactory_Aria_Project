import cv2 as cv
import numpy as np
from multiprocessing import Queue, Process
from pyzbar import pyzbar

CAM_ID = 0
CAM_WIDTH = 352  #480
CAM_HEIGHT = 288 #320

signal = 'N'
data = ""

### blue, red 영역의 from ~ to 값의 범위
lower_blue = np.array([90, 171, 149])
upper_blue = np.array([120,255,255])

lower_red1 = np.array([160, 50, 212]) 
upper_red1 = np.array([179, 255, 255])

lower_red2 = np.array([0, 65, 199])
upper_red2 = np.array([8, 255, 255])

# 카메라 실행
def open_cam(camera = CAM_ID):
    
    cap = cv.VideoCapture(camera)
    
    if cap.isOpened():
        cap.set(cv.CAP_PROP_FRAME_WIDTH, CAM_WIDTH) # 화면 크기 설정
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
    
    # BGR -> HSV로 변환
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 이미지에서 blue, red 영역
    mask_blue = cv.inRange(hsv_blue, lower_blue, upper_blue)
    mask_red1 = cv.inRange(hsv_red, lower_red1, upper_red1)
    mask_red2 = cv.inRange(hsv_red, lower_red2, upper_red2)

    mask_red = cv.add(mask_red1, mask_red2)
    
    erode_blue_image = cv.erode(mask_blue, None, iterations = 2)
    dilate_blue_image = cv.dilate(mask_blue, None, iterations = 2)
    
    erode_red_image = cv.erode(mask_red, None, iterations = 2)
    dilate_red_image = cv.dilate(mask_red, None, iterations = 2)
    
    return dilate_blue_image, dilate_red_image 

def detect_goods(filter_blue_image, filter_red_image, frame):
    contours_blue = cv.findContours(filter_blue_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    contours_red = cv.findContours(filter_red_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    if len(contours_blue) > 0:
        c = max(contours_blue, key=cv.contourArea)
        signal = 'P'    
        
    elif len(contours_red) > 0:
        c = max(contours_red, key=cv.contourArea)
        signal = 'F'
    
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
        (data, frame) = read_barcode(frame)
        #print("QRCODE: " + data + " signal: " + signal + "\n\n")
        cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv.circle(frame, (int(x), int(y)), 5, (0, 255, 255), -1)
        cv.putText(frame, str(x)+' , '+str(y), (x, y + 40), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2)
        return x, signal, data, frame
    
    else:
        #print("circle is too small \n\n")  

        x = -1
        y = -1
        data = ""
        return x, signal, data, frame

def read_barcode(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    barcode_data = ""
    
    if len(decoded) > 0:
        for d in decoded: 
            x, y, w, h = d.rect

            barcode_data = d.data.decode("utf-8")
            barcode_type = d.type
            text = '%s (%s)' % (barcode_data, barcode_type)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv.LINE_AA)
            
            return barcode_data, frame
    
    else:
        return barcode_data, frame    

def cam(cap):
    
    frame = cam_streaming(cap)

    frame = cv.GaussianBlur(frame, (1, 1), 0)
    
    (filter_blue_image, filter_red_image) = image_filter(frame)
    
    x, signal, data, frame = detect_goods(filter_blue_image, filter_red_image, frame)
    cv.rectangle(frame, (80, 0), (272, 288), (0, 0, 255), 2)
    
    cv.imshow('frame', frame)
    cv.imshow('filter_blue_mask', filter_blue_image)
    cv.imshow('filter_red_mask', filter_red_image)
    
    return x, signal, data        