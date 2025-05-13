import pymysql


def get_flag():
    conn = pymysql.Connect(
        host='47.93.91.229',
        port=3306,
        user='temu',
        passwd='aexyLEnRh83WFdA2',
        db='temu',
        charset='utf8')
    cursor = conn.cursor()
    sql = "select * from userinfo"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    print(get_flag())
