import pymysql


class MyConnection(object):

    def __init__(self):
        self.conn = pymysql.connect(host="192.168.84.128", port=3306, user="root", passwd="mysql", db="stock_db", charset="utf8")

    def __del__(self):
        print("__del__ 数据库连接关闭……")
        self.conn.close()

    def queryAllBySql(self, sql):
        cs = self.conn.cursor()
        cs.execute(sql)
        self.conn.commit()
        data = cs.fetchall()
        cs.close()
        return data
