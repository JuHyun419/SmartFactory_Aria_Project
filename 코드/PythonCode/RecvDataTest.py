import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump


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

_recvData = '''
<SECS2_XML_MESSAGE><HEAD><SystemByte>00001</SystemByte><CMD>3</CMD>
<Stream>2</Stream><Function>42</Function></HEAD><BODY><CEID>4</CEID>
<REPORTS><REPORT><REPORTID>400</REPORTID><VARIABLES><TEMP>25</TEMP>
<HUMID>50</HUMID></VARIABLES></REPORT></REPORTS></BODY></SECS2_XML_MESSAGE>
'''

tree = ET.fromstring(_recvData)
indent(tree)
dump(tree)
HEAD = tree.find('./HEAD')
Stream = HEAD.find('Stream')
Function = HEAD.find('Function')

BODY = tree.find('./BODY')
print(Stream.text, Function.text)

