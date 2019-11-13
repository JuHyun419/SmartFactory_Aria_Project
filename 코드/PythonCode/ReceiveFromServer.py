from socket import *

def ReceiveData():
    clientSock = socket(AF_INET, SOCK_STREAM)

    # 클라이언트에서 서버에 접속
    clientSock.connect(('127.0.0.1', 8099))

    # 서버에 데이터 전송
    clientSock.send("연결 합니다.".encode('utf-8'))
    data = clientSock.recv(1024)

    # decode('utf-8') : byte형식의 data를 str으로 변환
    print("받은 데이터 : ", data.decode('utf-8'))
    return data

data = ReceiveData()
print(data.decode('utf-8'))
print(type(data.decode('utf-8'))) 
