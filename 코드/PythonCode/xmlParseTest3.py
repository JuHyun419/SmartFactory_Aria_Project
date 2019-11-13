# XML을 객체화하기 위해 필요한 모듈
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
SubElement(body, "HCACK").text = "0"            # ff
#dump(root)
indent(root)    # xml 파일 보기좋게 만들기
dump(root)      
print(root.text)
# tree = ElementTree(root)    # ElementTree - XML 파일을 Element 객체의 트리로 로드, 저장
# tree.write('C:\Temp\AriaTest001.xml')   # 파일 저장

def send_s2f42(_systembyte, _hcack):
    root = Element('SECS2_XML_MESSAGE')
    head = SubElement(root, "HEAD")
    SubElement(head, "SystemByte").text = str(_systembyte)
    SubElement(head, "CMD").text = "3"
    SubElement(head, "Stream").text = "2"
    SubElement(head,"Function").text = "42"

    body = SubElement(root, "BODY")
    SubElement(body, "HCACK").text = str(_hcack)
    indent(root)    # xml 파일 보기좋게 만들기
    dump(root)      
    print(root.text)
    # socket send ( text )