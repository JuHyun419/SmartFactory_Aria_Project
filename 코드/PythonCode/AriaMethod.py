# XML을 객체화하기 위해 필요한 모듈
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
from socket import *
import xml.etree.ElementTree as ET


# 보기 좋게 XML 만드는 함수, 줄바꿈, 들여쓰기 작업
def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# 서버에 접속하는 함수
def connToServer(ServerIP, Port):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((ServerIP, Port))
    return clientSock


# Server -> PI  XML 형식으로 데이터를 받는 함수(S2F41)
def Receive_s2f41():
    clientSock = connToServer("127.0.0.1", 8099) # 서버에 접속
    data = clientSock.recv(1024)
    print("받은 데이터 : ", data.decode('utf-8'))
    tree = ET.parse('C:/Temp/AriaTest002.xml')
    HEAD = tree.find('./HEAD')          # HEAD를 검색한 후 마침
    Stream = HEAD.find('Stream')        # HEAD 루트노드중 Stream 찾기
    Function = HEAD.find('Function')    # HEAD 루트노드중 Function 찾기

    BODY = tree.find('./BODY')  # BODY를 검색
    RCMD = BODY.find('RCMD')    # BODY 루트노드중 RCMD 찾기
    return Stream, Function, RCMD


# PI -> Server  작업지시에 대한 응답
def Send_s2f42(_SystemByte, _Hcack):
    clientSock = connToServer("127.0.0.1", 8099) # 서버에 접속
    root = Element("SECS2_XML_MESSAGE")

    ## HEAD
    head = SubElement(root, "HEAD")
    SubElement(head, "SystemByte").text = str(_SystemByte)
    SubElement(head, "CMD").text = "3"
    SubElement(head, "Stream").text = "2"
    SubElement(head,"Function").text = "42"

    ## BODY
    body = SubElement(root, "BODY")
    SubElement(body, "HCACK").text = str(_Hcack)

    indent(root)    # indent() : XML 형식으로 보기 좋게 만들어주는 함수
    dump(root)      # dump 함수는 인자로 넘어온 tag 이하를 print 해줌
    clientSock.send((root.text).encode('utf-8'))    # Server로 데이터 전송
    print(root.text)


# PI -> Server  Lot 작업 시작 전송
def Send_s6f11_Lot(_SystemByte, _CEID, _LOTID):
     clientSock = connToServer("127.0.0.1", 8099) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = str(_SystemByte)
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = str(_CEID)
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(body, "REPORTID").text = "200"
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "LOT_ID").text = _LOTID

     indent(root)    # indent() : XML 형식으로 보기 좋게 만들어주는 함수
     dump(root)      # dump 함수는 인자로 넘어온 tag 이하를 print 해줌
     clientSock.send((root.text).encode('utf-8'))    # Server로 데이터 전송
     print(root.text)


# PI -> Server  1개의 제품 생산 완료 전송
def Send_s6f11_Complete(_SystemByte, _CEID):
     clientSock = connToServer("127.0.0.1", 8099) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = str(_SystemByte)
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = str(_CEID)
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(body, "REPORTID").text = "100"
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "LOT_ID").text = "A"
     SubElement(variables, "PRODUCTID").text = "A"
     SubElement(variables, "STATE").text = "A"
     SubElement(variables, "LOT_ID").text = "A"
     SubElement(variables, "LOT_ID").text = "A"
     SubElement(variables, "LOT_ID").text = "A"

     clientSock.send((root.text).encode('utf-8'))    # Server로 데이터 전송
     print(root.text)
     

# -----------------------------------------------------------------
# XML 형식
#   <SECS2_XML_MESSAGE>
#     <HEAD>
#       <SystemByte> 00006 </SystemByte>
#       <CMD> 3 </CMD>
#       <Stream> 6 </Stream>
#       <Function> 11 </Function>
#     </HEAD>
#     <BODY>
#       <CEID> 4 </CEID> // Line_Env_Update
#       <REPORTS>
#         <REPORT>
#           <REPORTID> 400 </REPORTID>
#           <VARIABLES>
#             <V> 26 </V>
#             <V> 51 </V>
#           </VARIABLES>
#         </REPORT>
#       </REPORTS>
#     </BODY>
#   </SECS2_XML_MESSAGE>
# -----------------------------------------------------------------

## PI -> Server  라인 환경 정보 업데이트(온습도)
def Send_s6f11_TempHumid(_SystemByte, _CEID, _Temp, _Humid):
     clientSock = connToServer("220.69.249.231", 8099) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = str(_SystemByte)
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = str(_CEID)     # CEID
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "400"    # REPORTID
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "TEMP").text = str(_Temp)    # TEMP
     SubElement(variables, "HUMID").text = str(_Humid)  # HUMID

     #indent(root)
     data = ET.tostring(root, encoding='utf-8', method='xml')
     clientSock.send(str(data).encode('utf-8'))    # Server로 데이터 전송

Send_s6f11_TempHumid(1, 4, 25, 50)
    
