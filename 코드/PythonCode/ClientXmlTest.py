# XML을 객체화하기 위해 필요한 모듈
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import xml.etree.ElementTree as ET
from socket import *

root = Element('SECS2_XML_MESSAGE')
head = SubElement(root, "HEAD")
SubElement(head, "SystemByte").text = "00001"   # ff
SubElement(head, "CMD").text = "3"
SubElement(head, "Stream").text = "2"
SubElement(head,"Function").text = "42"

body = SubElement(root, "BODY")
SubElement(body, "CEID").text = "4"            # ff
reports = SubElement(body, "REPORTS")
report = SubElement(reports, "REPORT")
SubElement(report, "REPORTID").text = "400"
variables = SubElement(report, "VARIABLES")
SubElement(variables, "TEMP").text = "25"
SubElement(variables, "HUMID").text = "50"

data = ET.tostring(root, encoding='utf-8', method='xml')
print(data)

clientSock = socket(AF_INET, SOCK_STREAM)

# 클라이언트에서 서버에 접속
clientSock.connect(('127.0.0.1', 8099))

print('연결 확인 됐습니다.')

# 서버에게 데이터 전송
clientSock.send(data)    # encode() - 문자열을 byte로 변환

print('메시지를 전송했습니다.')

# 서버로부터 데이터 받음
data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))