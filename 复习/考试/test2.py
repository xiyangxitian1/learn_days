"""
-- 创建数据库并使用
create database heima charset = utf8;
use heima;

-- 创建users表
create table users (
    id int(10) primary key auto_increment,
    name varchar(20) not null unique,
    age int(3),
    sex char(1),
    phone_num varchar(20)
);
"""
# 要求4: 输入1进入添加模块，依次提示用户输入用户名、年龄、性别、电话号码，若全部输入正确，
# 将该用户名和密码信息存入数据库，提示“添加成功”并返回主页面；
# 若数据库中已存在该用户名，提示“该用户名已存在, 请重新添加!”
#
# 要求5: 输入2进入查询模块，提示用户输入要查询的用户名，输入正确，返回该用户的信息；若用户名输入错误，提示“用户名错误, 请重新输入!”
#
import pymysql
import re


# conn = pymysql.connect(host="192.168.84.128", port=3306, user="root", password="mysql", database="heima",
#                        charset="utf8")

class MyConnection(object):

    def __init__(self, host, port, user, password, database):
        conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                               charset="utf8")
        self.conn = conn

    def __del__(self):
        self.conn.close()


def add():
    myConnection = MyConnection(host="192.168.84.128", port=3306, user="root", password="mysql", database="heima")
    conn = myConnection.conn
    while True:
        # 用户名、年龄、性别、电话号码
        name = input("请输入用户名：")
        age = input("请输入年龄：")
        sex = input("请输入性别：")
        phone = input("请输入电话号码：")
        cs = conn.cursor()
        cs.execute("select count(1) from users where name = %s ", args=[name])
        count = cs.fetchone()
        if count[0] != 0:
            print("该用户名已存在, 请重新添加!")
            continue
        if not age.isdigit() or int(age) > 150 or int(age) < 1:
            print("年龄不合规，请重新输入！")
            continue
        if not (sex == "男" or sex == "女"):
            print("性别输入不正确，请重新输入")
            continue
        result = re.match("^1[3-9][0-9]{9}$", phone)
        if not result:
            print("请输入正确的11位手机号")
            continue

        # inser into users values(0,'张三',22,'男',12342352);
        cs.execute("insert into users values (0,%s,%s,%s,%s)", args=[name, age, sex, phone])
        conn.commit()
        print("添加成功")
        break
    cs.close()


def query():
    myConnection = MyConnection(host="192.168.84.128", port=3306, user="root", password="mysql", database="heima")
    conn = myConnection.conn
    while True:
        name = input("输入要查询的用户名:")
        cs = conn.cursor()
        cs.execute("select * from users where name = %s ", args=[name])
        conn.commit()
        datas = cs.fetchone()
        if len(datas) != 0:
            print(datas)
            break
        else:
            print("用户名错误, 请重新输入!")
            continue
    cs.close()


def main():
    """程序入口"""
    while True:
        print("-" * 7, "会员管理系统", "-" * 7)
        print("1: 添加会员")
        print("2: 查询会员")
        print("3: 退出系统")
        num = input("请输入功能对应的序号：").strip()
        if not (num == "1" or num == "2" or num == "3"):
            print("您输入的不正确，请重新输入（只能是1或2或3）")
            continue
        if num == "1":
            add()
        elif num == "2":
            query()
        else:
            break


if __name__ == '__main__':
    main()
