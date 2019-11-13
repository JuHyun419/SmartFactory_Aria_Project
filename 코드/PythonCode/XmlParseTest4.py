# XML을 객체화하기 위해 필요한 모듈
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
import xml.etree.ElementTree as ET
import re


# 보기 좋게 xml 만드는 함수, 줄바꿈, 들여쓰기 작업
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



xmlStr = '''
            <users>
                    <user grade="gold">
                        <name>LeeJuHyun</name>
                        <age>19</age>
                        <birthday>20010419</birthday>
                    </user>
                    <user grade="diamond">
                        <name>LeeJuHyun2</name>
                        <age>20</age>
                        <birthday>20000419</birthday>
                    </user>
            </users>
        '''


#          xml 파일 형식
# --------------------------------
# <SECS2_XML_MESSAGE>
#   <HEAD>
#     <SystemBtye>00001</SystemBtye>
#     <CMD>3</CMD>
#     <Stream>2</Stream>
#     <Function>42</Function>
#   </HEAD>
#   <BODY>
#     <HCACK>0</HCACK>
#     <temp> ~ </temp>
#     <humid> ~ </humid>
#   </BODY>
# </SECS2_XML_MESSAGE>
# --------------------------------

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
#dump(root)
# indent(root)    # xml 파일 보기좋게 만들기
#dump(root)      
print('---------------------------------')
data = ET.tostring(root, encoding='utf-8', method='xml')
#print(data)
print('---------------------------------')
#str_data = str(data)

print(data)
print(type(data))
str_data = str(data)



str_data2 = str_data.replace("b", "").replace("'", "")
print(str_data2)

tree = ET.fromstring(str_data2)
indent(tree)
dump(tree)



#recv_data = 
#print(recv_data)


# tree = ET.fromstring(xmlStr)     
# indent(tree)
# dump(tree)               

#tree = ET.fromstring(str_data.encode("utf-8"))
