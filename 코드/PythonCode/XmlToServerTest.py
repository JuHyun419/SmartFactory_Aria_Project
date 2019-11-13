from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('220.69.249.231', 4000))
temp = str(15)
humid = str(28)
Color = str(1)

def xmlStrr():
    xmlStr ='''
        <SECS2_XML_MESSAGE>
            <HEAD>
                <SystemByte>00001</SystemByte>
                <CMD>3</CMD>
                <Stream>2</Stream>
                <Function>42</Function>
            </HEAD>
            <BODY>
                <HCACK>0</HCACK>
                <TEMP>'''  + temp  + '''</TEMP>
                <HUMID>''' + humid + '''</HUMID>
                <COLOR>''' + Color + '''</COLOR>
            </BODY>
        </SECS2_XML_MESSAGE>
        '''
    return xmlStr

xmlStr = xmlStrr()
clientSock.send(xmlStr.encode('utf-8'))
print(xmlStr)