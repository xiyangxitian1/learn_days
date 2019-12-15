import pymysql


def conn_mysql():
    params = {
        "host": "192.168.84.128",
        "port": 3306,
        "user": "root",
        "passwd": "mysql",
        "db": "jing_dong",
        "charset": "utf8"
    }
    conn = pymysql.connect(**params)
    try:
        cs = conn.cursor()
        sql = """
        select * from goods;
        """
        cs.execute(sql)
        conn.commit()
        datas = cs.fetchone()
        # print("datas:", datas)
        for data in datas:
            print(data)
    except Exception as e:
        print(e)
    finally:
        cs.close()
        conn.close()

if __name__ == '__main__':
    conn_mysql()