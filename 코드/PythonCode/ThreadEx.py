import threading

# 메신저 - 송신 코드와 수신 코드는 어느 하나가 끝날때까지
# 기다릴 필요가 없이 별개로 작동해도 된다.
class Messenger(threading.Thread):

    # 파이썬 Thread에서 Thread를 구동하기 위해서는 함수명을 run으로 해주어야 함
    def run(self):

        # 10번 반복, 변수를 지정하지 않고 단순 반복 구현 - 언더바(_)
        for _ in range(10):

            # 현재 구동되고 있는 Thread의 이름 출력
            # 서로다른 Thread가 반복문을 참조할때, 어떤 Thread인지 확인
            print(threading.currentThread().getName())

send = Messenger(name = 'Sending out messages')
recv = Messenger(name = 'Receiving messages')

# 각 Thread 시작
send.start()
recv.start()