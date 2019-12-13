import time

my_dict = {}

def route(path):
    def dectator(fn):
        my_dict[path] = fn

        def inner():
            fn()

        return inner

    return dectator


# "/index.html": index,
# "/center.html": center
@route("/index.html")
def index():
    # return time.ctime()
    with open('template/index.html', 'rb') as f:
        return f.read()


@route("/center.html")
def center():
    with open('template/center.html', 'rb') as f:
        return f.read()


def not_found():
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


def handle_req(request_path):
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # # 响应头
    response_header = "Server: PWS2.0\r\n"
    # # 响应体
    response_body = ""
    fun = my_dict.get(request_path)
    if fun:
        response_body = fun()
        # 拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        return response_data
    else:
        """找不到"""
        return not_found()
