import time as time1
import datetime as dt

now = time1.localtime()


print("---------------------------------------------")
now = time1.localtime()
print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
print("MES Server로 부터 명령을 받았습니다.")
print("---------------------------------------------")


