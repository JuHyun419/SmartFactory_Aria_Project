# XML로 파싱하기(xml 파일형태로 존재)

import xml.etree.ElementTree as etree

tree = etree.parse('C:/Temp/AriaTest002.xml')
head = tree.find('./HEAD')  # HEAD를 검색한 후 마침

print(head.tag) # HEAD 출력
systemByte = head.find('SystemByte')    # HEAD 노드 안에서 SystemByte 요소 찾기
cmd = head.find('CMD')                  # HEAD 노드 안에서 CMD 요소 찾기
stream = head.find('Stream')            # HEAD 노드 안에서 Stream 요소 찾기


print(systemByte.text, cmd.text, stream.text)
