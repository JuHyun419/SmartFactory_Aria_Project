import socket   # socket 모듈 불러오기

def run_server(port=4000):  # 포트=4000 임의로 저장
    host = '127.0.0.1'      # 호스트

    # 소켓 선언
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))    # 소켓 바인드(호스트, 포트)
        s.listen(1)             # 클라이언트 연결을 받는 상태
        conn, addr = s.accept() # 클라이언트로부터 소켓과 클라이언트 주소 반환
        msg = conn.recv(1024)   # 연결된 클라이언트로부터 데이터 받음(1024)
        print(f'{msg.decode()}')    # 받은 데이터 출력
        conn.sendall(msg)       # 데이터 재전송
        conn.close()            # 연결 종료

if __name__ == '__main__':
    run_server()