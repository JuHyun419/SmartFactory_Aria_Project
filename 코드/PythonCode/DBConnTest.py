import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host = '192.168.111.226', user='root', password='1234', db='Aria', charset='utf8')
try:
    curs = conn.cursor()    # Connection 으로부터 Cursor 생성
    sql = "SELECT * FROM users"    # SQL문
    curs.execute(sql)  # SQL문 실행
    result = curs.fetchall()
    conn.commit()   # 테이블 커밋

    for i in result:
        print(i)

# 오류가 발생해도 반드시 실행
finally:
    conn.close()    # DB 연결 종료
