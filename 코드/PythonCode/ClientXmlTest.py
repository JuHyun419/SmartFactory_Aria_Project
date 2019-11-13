# XML을 객체화하기 위해 필요한 모듈
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import xml.etree.ElementTree as ET
from socket import *

root = Element("SECS2_XML_MESSAGE")

## HEAD
head = SubElement(root, "HEAD")
SubElement(head, "SystemByte").text = "00001"
SubElement(head, "CMD").text = "3"
SubElement(head, "Stream").text = "6"
SubElement(head,"Function").text = "11"

## BODY
body = SubElement(root, "BODY")
SubElement(body, "CEID").text = "1"
reports = SubElement(body, "REPORTS")

## REPORT
report = SubElement(reports, "REPORT")
SubElement(body, "REPORTID").text = "100"
variables = SubElement(report, "VARIABLES")
SubElement(variables, "Product_number").text = "AA"
SubElement(variables, "Model_name").text = "BB"
SubElement(variables, "Model_temp").text = "CC"
SubElement(variables, "Model_humid").text = "DD"
SubElement(variables, "Color").text = "FF"
SubElement(variables, "Fail_reason").text = "AA"
SubElement(variables, "QRCode").text = "BB"
SubElement(variables, "CV_move_state").text = "Start"
SubElement(variables, "Robot_gripper_state").text = "Start"

data = ET.tostring(root, encoding='utf-8', method='xml')

clientSock = socket(AF_INET, SOCK_STREAM)

# 클라이언트에서 서버에 접속
clientSock.connect(('127.0.0.1', 8099))
#clientSock.connect(('220.69.249.226', 4000))

print('연결 확인 됐습니다.')

str_data = str(data)
str_data2 = str_data.replace("b", "").replace("'", "")

# 서버에게 데이터 전송
clientSock.send(data)    # encode() - 문자열을 byte로 변환

print('메시지를 전송했습니다.')

# 서버로부터 데이터 받음
data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))