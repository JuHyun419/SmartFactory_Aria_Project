# from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
# import xml.etree.ElementTree as ET


# # 보기 좋게 XML 만드는 함수, 줄바꿈, 들여쓰기 작업
# def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
#     i = "\n" + level*"  "
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text = i + "  "
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#         for elem in elem:
#             indent(elem, level+1)
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = i


# root = Element("SECS2_XML_MESSAGE")

# ## HEAD
# head = SubElement(root, "HEAD")
# SubElement(head, "SystemByte").text = "00001"
# SubElement(head, "CMD").text = "3"
# SubElement(head, "Stream").text = "6"
# SubElement(head,"Function").text = "11"

# ## BODY
# body = SubElement(root, "BODY")
# SubElement(body, "CEID").text = "4"     # CEID
# reports = SubElement(body, "REPORTS")

# ## REPORT
# report = SubElement(reports, "REPORT")
# SubElement(report, "REPORTID").text = "400"    # REPORTID
# variables = SubElement(report, "VARIABLES")
# SubElement(variables, "Temp").text = "15"    # TEMP
# SubElement(variables, "Humid").text = "20"  # HUMID

# indent(root)
# dump(root)

# # data = ET.tostring(root, encoding='utf-8', method='xml')
# # print(type(data))
# # str_data = str(data)
# # print(str_data)

for i in range(1):
    print(i)