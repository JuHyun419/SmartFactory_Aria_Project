from socket import *
import xml.etree.ElementTree as ET

# 소캣 객체 생성, 첫번째 인자 : 주소체계, 두번째 인자 : 소켓 타입
serverSock = socket(AF_INET, SOCK_STREAM)

# bind() - 생성된 소켓의 번호와 실제 어드레스 패밀리를 연결
serverSock.bind(('', 8099)) # '' 공백 : 모든 인터페이스와 연결

# (1) -> 해당 소켓이 총 몇개의 동시접속까지 허용할지 나타낼 숫자
# 서버 소켓은 상대방의 접속이 올때까지 대기하는 상태
serverSock.listen(1)

# 소켓에 누군가의 연결 허용
connectionSock, addr = serverSock.accept()

# 연결된 상대방의 주소 출력
print(str(addr),'에서 접속이 확인되었습니다.')

# 클라이언트로부터 데이터 받음
data = connectionSock.recv(1024)
print('받은 데이터 : ', data)   # encode() - 문자열을 byte로 변환

# 클라이언트에게 데이터 전송
connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')

print(type(str(data)))
str_data = str(data)
