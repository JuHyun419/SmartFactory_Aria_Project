from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)

# 클라이언트에서 서버에 접속
clientSock.connect(('127.0.0.1', 8099))

print('연결 확인 됐습니다.')
data = "I am a Client"

# 서버에게 데이터 전송
clientSock.send(data.encode('utf-8'))    # encode() - 문자열을 byte로 변환

print('메시지를 전송했습니다.')

# 서버로부터 데이터 받음
data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))