import pymysql.cursors

# config = {
#     'host' : '192.168.111.226'
#     'user' : 'root'
#     'password' : '1234'
#     'db' : 'Aria'
#     'charset' = 'utf8'
# }

conn = pymysql.connect(host='192.168.111.226', user='root', password='1234', db='Aria', charset='utf8')
def Insert(user_id, pass_word, LEVEL, e_mail, first_name, last_name):
    try:
        curs = conn.cursor()
        sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
        val = ("AB", "AB", 1, "AB", "AB", "AB")
        curs.execute(sql, val)
        conn.commit()
    finally:
        conn.close()
