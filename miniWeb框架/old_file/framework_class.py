import json
import logging
from mysql_util.mysql_util import MyConnection

my_dict = {}


# def route(path):
#     def dectator(fn):
#         my_dict[path] = fn
#
#         def inner(*args, **kwargs):
#             fn(*args, **kwargs)
#
#         return inner
#
#     return dectator
# 类装饰器，一般用函数就可以了
class route(object):
    def __init__(self, path):
        self.__path = path

    def __call__(self, fn):
        my_dict[self.__path] = fn

        def wrapper(*args, **kwargs):
            fn(*args, **kwargs)

        return wrapper


class FrameWork(object):

    # "/index.html": index,
    # "/center.html": center

    def __init__(self):
        self.dict = my_dict

    # 个人中心数据接口开发
    @route("/center_data.html")
    def center_data(self):
        # 响应状态
        status = "HTTP/1.1 200 OK\r\n"
        # 响应头
        # "Content-Type", "text/html;charset=utf-8\r\n" 这个是告诉浏览器，显示的形式，实际中这东西也不需要。只返回JSON数据
        response_header = [("Server", "PWS2.0\r\n"), ("Content-Type", "text/html;charset=utf-8\r\n")]
        headers = ""
        for r in response_header:
            headers += r[0] + ":" + r[1]
        # 查询sql语句
        sql = """select i.code, i.short, i.chg, 
                 i.turnover, i.price, i.highs, f.note_info 
                 from info as i inner join focus as f on i.id = f.info_id"""
        result = MyConnection().queryAllBySql(sql)
        # 个人中心数据列表
        center_data_list = list()
        # 遍历每一行数据转成字典
        for row in result:
            # 创建空的字典
            center_dict = dict()
            center_dict["code"] = row[0]
            center_dict["short"] = row[1]
            center_dict["chg"] = row[2]
            center_dict["turnover"] = row[3]
            center_dict["price"] = str(row[4])
            center_dict["highs"] = str(row[5])
            center_dict["note_info"] = row[6]
            # 添加每个字典信息
            center_data_list.append(center_dict)

        # 把列表字典转成json字符串, 并在控制台显示
        json_str = json.dumps(center_data_list, ensure_ascii=False)
        print(json_str)
        response_data = (status + headers + "\r\n" + json_str).encode("utf-8")
        # return status, headers, json_str
        return response_data

    @route("/index.html")
    def index(self):
        # return time.ctime()
        with open('template/index.html', 'r', encoding='utf-8') as f:
            data = f.read()

        sql = "select * from info"
        conn = MyConnection()
        data_by_sql = conn.queryAllBySql(sql)
        data_on_sql = ""
        for d in data_by_sql:
            data_on_sql += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type='button' value='添加'/>
                    <input type='button' value='修改'/>
                </td>
            </tr>
            """ % d
        data = data.replace("{%content%}", data_on_sql)
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # # 响应头
        response_header = "Server: PWS2.0\r\n"
        response_body = data
        # # 响应体
        response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
        return response_data

    @route("/center.html")
    def center(self):
        data = ""
        with open('template/center.html', 'r', encoding='utf-8') as f:
            data = f.read()
        # data = data.replace("{%content%}", time.ctime())
        data = data.replace("{%content%}", "")
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # # 响应头
        response_header = "Server: PWS2.0\r\n"
        response_body = data
        # # 响应体
        response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
        return response_data

    def not_found(self):
        # 响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应头
        response_header = "Server: PWS2.0\r\n"
        # 响应体
        response_body = "not found"

        # 拼接响应报文
        response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
        # return "HTTP/1.1 404 Not Found\r\n"
        return response_data

    def handle_req(self, request_path):
        fun = self.dict.get(request_path)
        # print("fun", fun)
        if fun:
            logging.info("根据路由找到方法：" + str(fun))
            response_data = fun(self)
            # 拼接响应报文
            return response_data
        else:
            """找不到"""
            logging.warning("找不到请求路径%s对应的方法" % request_path)
            return self.not_found()
