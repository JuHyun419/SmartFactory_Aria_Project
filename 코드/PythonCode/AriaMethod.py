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


# XML 형식의 문자열
_recvData = '''
<SECS2_XML_MESSAGE><HEAD><SystemByte>00001</SystemByte><CMD>LOT_START</CMD>
<Stream>2</Stream><Function>41</Function></HEAD><BODY>
<Model_name>아리아크림빵</Model_name><Prod_count>10</Prod_count><Model_temp>19</Model_temp>
<Model_humid>21</Model_humid>
<Color>Blue</Color></BODY></SECS2_XML_MESSAGE>
'''


## 문자열 -> Xml 객체로 파싱하는 함수
# Model_name  : 아리아크림빵,
# Prod_count  : 상품 개수
# Color       : 상품 색상
def Receive_s2f41(recvData):
    tree = ET.fromstring(recvData)   # 문자열 -> Xml 객체
    indent(tree)    # Xml을 보기좋게 만드는 함수
    BODY = tree.find('./BODY')  # XML에서 BODY 루트 찾기

    # BODY 노드에서 각 루트 찾기
    Model_name = BODY.find('Model_name')
    Prod_count = BODY.find('Prod_count')
    # Model_temp = BODY.find('Model_temp')
    # Model_humid = BODY.find('Model_humid')
    Color = BODY.find('Color')
    
    # Element 형식을 str으로 형변환 해서 리턴
    return str(Model_name.text), str(Prod_count.text), str(Color.text)


# PI -> Server  작업지시에 대한 응답
def Send_s2f42(ServerIP, Port, SystemByteResult):
    clientSock = connToServer(ServerIP, Port) # 서버에 접속
    root = Element("SECS2_XML_MESSAGE")

    ## HEAD
    head = SubElement(root, "HEAD")
    SubElement(head, "SystemByte").text = SystemByteResult
    SubElement(head, "CMD").text = "3"
    SubElement(head, "Stream").text = "2"
    SubElement(head,"Function").text = "42"

    ## BODY
    body = SubElement(root, "BODY")
    SubElement(body, "HCACK").text = "0"

    # XML 형식을 bytes로 변환
    data = ET.tostring(root, encoding='utf-8', method='xml')

    # indent(root)    # indent() : XML 형식으로 보기 좋게 만들어주는 함수
    # dump(root)      # dump 함수는 인자로 넘어온 tag 이하를 print 해줌
    clientSock.send(data)    # Server로 데이터 전송(bytes)
    print(root.text)


# -----------------------------------------------------------------
# XML 형식
#   <SECS2_XML_MESSAGE>
#     <HEAD>
#       <SystemByte> 00001 </SystemByte>
#       <CMD> 3 </CMD>
#       <Stream> 6 </Stream>
#       <Function> 11 </Function>
#     </HEAD>
#     <BODY>
#       <CEID> 1 </CEID> // Line_Env_Update
#       <REPORTS>
#         <REPORT>
#           <REPORTID> 100 </REPORTID>
#           <VARIABLES>
#            <Product_number> 01, 02, 10, 20, ... </Product_number>
#            <Model_name> 아리아크림빵,아리아메론빵 </Model_name>
#            <Prod_Percent> 1/10 </Prod_Percent>
#	         <Result> "Pass" or "Fail" </Result>
#        	 <Fail_reason> reason </Fail_reason>
#	         <C/V move state> 임의값 </C/V move state>
#	         <Robot gripper state> 임의값 </Robot gripper state>
#           </VARIABLES>
#         </REPORT>
#       </REPORTS>
#     </BODY>
#   </SECS2_XML_MESSAGE>
# -----------------------------------------------------------------

# PI -> Server  1개의 정상 제품 생산 완료 전송(CEID = 1)
def Send_s6f11_Complete_Blue(ServerIP, Port, SystemByteResult, Product_number, Model_name, Prod_Percent):
     clientSock = connToServer(ServerIP, Port) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = SystemByteResult
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = "1"
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "100"
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "Product_number").text = str(Product_number)
     SubElement(variables, "Model_name").text = str(Model_name)
     SubElement(variables, "Prod_Percent").text = str(Prod_Percent)
     SubElement(variables, "Result").text = "Pass"
     SubElement(variables, "Fail_reason").text = " "
     SubElement(variables, "C/V move state").text = "Start"
     SubElement(variables, "Robot gripper state").text = "Start"

     # XML 형식을 bytes로 변환
     data = ET.tostring(root, encoding='utf-8', method='xml')

     #  str_data = str(data)   # 문자열로 변환
     #  str_data2 = str_data.replace("b", "").replace("'", "") # 문자열 중 b' 제거

     clientSock.send(data)    # Server로 데이터 전송


# -----------------------------------------------------------------
# XML 형식
#   <SECS2_XML_MESSAGE>
#     <HEAD>
#       <SystemByte> 00001 </SystemByte>
#       <CMD> 3 </CMD>
#       <Stream> 6 </Stream>
#       <Function> 11 </Function>
#     </HEAD>
#     <BODY>
#       <CEID> 1 </CEID> // Line_Env_Update
#       <REPORTS>
#         <REPORT>
#           <REPORTID> 100 </REPORTID>
#           <VARIABLES>
#            <Product_number> 01, 02, 10, 20, ... </Product_number>
#            <Model_name> 아리아크림빵,아리아메론빵 </Model_name>
#            <Prod_Percent> 1/10 </Prod_Percent>
#	         <Result> "Pass" or "Fail" </Result>
#        	 <Fail_reason> reason </Fail_reason>
#	         <C/V move state> 임의값 </C/V move state>
#	         <Robot gripper state> 임의값 </Robot gripper state>
#           </VARIABLES>
#         </REPORT>
#       </REPORTS>
#     </BODY>
#   </SECS2_XML_MESSAGE>
# -----------------------------------------------------------------
# PI -> Server  1개의 불량 제품 생산 완료 전송(CEID = 1)
def Send_s6f11_Complete_Red(ServerIP, Port, SystemByteResult, Product_number, Model_name, Prod_Percent):
     clientSock = connToServer(ServerIP, Port) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = SystemByteResult
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = "1"
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "100"
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "Product_number").text = str(Product_number)
     SubElement(variables, "Model_name").text = str(Model_name)
     SubElement(variables, "Prod_Percent").text = str(Prod_Percent)
     SubElement(variables, "Result").text = "Fail"
     SubElement(variables, "Fail_reason").text = "Red"
     SubElement(variables, "C/V move state").text = "Start"
     SubElement(variables, "Robot gripper state").text = "Start"

     # XML 형식을 bytes로 변환
     data = ET.tostring(root, encoding='utf-8', method='xml')

     #  str_data = str(data)   # 문자열로 변환
     #  str_data2 = str_data.replace("b", "").replace("'", "") # 문자열 중 b' 제거

     clientSock.send(data)    # Server로 데이터 전송


# -----------------------------------------------------------------
# XML 형식
#   <SECS2_XML_MESSAGE>
#     <HEAD>
#       <SystemByte> 00002 </SystemByte>
#       <CMD> 3 </CMD>
#       <Stream> 6 </Stream>
#       <Function> 11 </Function>
#     </HEAD>
#     <BODY>
#       <CEID> 2 </CEID>
#       <REPORTS>
#         <REPORT>
#           <REPORTID> 200 </REPORTID>
#         </REPORT>
#       </REPORTS>
#     </BODY>
#   </SECS2_XML_MESSAGE>
# -----------------------------------------------------------------

# PI -> Server  Lot 작업 시작 전송(CEID = 2)
def Send_s6f11_Lot_Start(ServerIP, Port, SystemByteResult):
     clientSock = connToServer(ServerIP, Port) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = SystemByteResult
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = "2"
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "200"

     # XML 형식을 bytes로 변환
     data = ET.tostring(root, encoding='utf-8', method='xml')
     clientSock.send(data)    # Server로 데이터 전송


# PI -> Server  Lot 명령에 대한 모든 제품을 생산 완료함(CEID = 3)
def Send_s6f11_Lot_Complete(ServerIP, Port, SystemByteResult):
     clientSock = connToServer(ServerIP, Port) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = SystemByteResult
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = "3"
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "300"

     # XML 형식을 bytes로 변환
     data = ET.tostring(root, encoding='utf-8', method='xml')
     clientSock.send(data)    # Server로 데이터 전송


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

## PI -> Server  라인 환경 정보 업데이트(온습도, CEID = 4)
def Send_s6f11_TempHumid(ServerIP, Port, SystemByteResult, Temp, Humid):
     clientSock = connToServer(ServerIP, Port) # 서버에 접속
     root = Element("SECS2_XML_MESSAGE")

     ## HEAD
     head = SubElement(root, "HEAD")
     SubElement(head, "SystemByte").text = SystemByteResult
     SubElement(head, "CMD").text = "3"
     SubElement(head, "Stream").text = "6"
     SubElement(head,"Function").text = "11"

     ## BODY
     body = SubElement(root, "BODY")
     SubElement(body, "CEID").text = "4" 
     reports = SubElement(body, "REPORTS")

     ## REPORT
     report = SubElement(reports, "REPORT")
     SubElement(report, "REPORTID").text = "400"    # REPORTID
     variables = SubElement(report, "VARIABLES")
     SubElement(variables, "Temp").text = str(Temp)    # TEMP
     SubElement(variables, "Humid").text = str(Humid)  # HUMID

     #indent(root)
     data = ET.tostring(root, encoding='utf-8', method='xml')
     clientSock.send(data)    # Server로 데이터 전송

