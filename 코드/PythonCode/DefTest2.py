import time as time1        # 타임 관련 라이브러리
Model_name = "Aria Cream"
Prod_count = 10
Color = "Blue"

print("제품명 : " + Model_name)


print("------------------------------")
now = time1.localtime()
print("현재시간 : %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
print("MES Server로 부터 Start 명령을 받았습니다.")
print("------------------------------")


print("제품이름 : " + Model_name)
print("제품수량 : " + str(Prod_count))
print("제품색상 : " + Color)