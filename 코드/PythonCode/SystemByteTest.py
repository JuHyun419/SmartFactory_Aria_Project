# 00001, 00002, 00003, 00004, 00005, ..., 00010
SystemByte = [0, 0, 0, 0, 0]

# 00001 부터 1씩 증가하는 함수
def _SystemBytePlus():
    SystemByte[4] +=1   # 일의자리 1씩 증가
    if(SystemByte[4] == 10):    # 일의자리가 10이 됬을때
        SystemByte[3] += 1      # 십의자리 +1
        SystemByte[4] = 0       # 일의자리 초기화
    
    if(SystemByte[3] == 10):    # 십의자리가 10이 됬을때
        SystemByte[2] += 1      # 백의자리 +1
        SystemByte[3] = 0       # 십의자리 초기화
    
    if(SystemByte[2] == 10):    # 백의자리가 10이 됬을때
        SystemByte[1] += 1      # 천의자리 +1
        SystemByte[2] = 0       # 백의자리 초기화

    if(SystemByte[1] == 10):    # 천의자리가 10이 됬을때
        SystemByte[0] += 1      # 만의자리 +1
        SystemByte[1] = 0       # 천의자리 초기화
    
    _SystemByte = str(SystemByte[0]) + str(SystemByte[1]) + str(SystemByte[2]) + str(SystemByte[3]) + str(SystemByte[4])
    return _SystemByte

for i in range(10000):
    print(_SystemBytePlus())
