import socket
import threading
import sys
import framework
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    # filename="log.txt",
                    # filemode="w"
                    )


# 定义web服务器类
class HttpWebServer(object):

    def __init__(self, port):
        """init """
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户的请求
    @staticmethod
    def handle_client_request(new_socket, ip_port):
        # 代码执行到此，说明连接建立成功
        logging.info("连接成功：" + str(ip_port))
        recv_client_data = new_socket.recv(4096);
        if recv_client_data:
            # 对二进制数据进行解码
            recv_client_content = recv_client_data.decode("utf-8")
            logging.info("接收到的数据" + recv_client_content)
            # 根据指定字符串进行分割， 最大分割次数指定2
            request_list = recv_client_content.split(maxsplit=2)
            request_path = request_list[1]
            logging.info("请求资源路径:" + request_path)
            # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
            if request_path == "/":
                request_path = "/index.html"
            # 判断是否是动态资源请求
            if request_path.endswith(".html"):
                """这里是动态资源请求，把请求信息交给框架处理"""
                # 字典存储用户的请求信息
                env = {
                    "request_path": request_path
                }
                # 获取处理结果
                status, headers, response_body = framework.handle_request(env)
                # 使用框架处理的数据拼接响应报文
                # 响应行
                response_line = "HTTP/1.1 %s\r\n" % status
                # 响应头
                response_header = ""
                # 遍历头部信息
                for header in headers:
                    # 拼接多个响应头
                    response_header += "%s: %s\r\n" % header
                response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
                # 发送数据
                new_socket.send(response_data)
                # 关闭socket
                new_socket.close()
            else:
                """这里是静态资源请求"""
                try:
                    # 动态打开指定文件
                    with open("../static" + request_path, "rb") as file:
                        # 读取文件数据
                        file_data = file.read()
                except Exception as e:
                    # 请求资源不存在，返回404数据
                    # 响应行
                    response_line = "HTTP/1.1 404 Not Found\r\n"
                    # 响应头
                    response_header = "Server: PWS1.0\r\n"
                    with open("../static/error.html", "rb") as file:
                        file_data = file.read()
                    # 响应体
                    response_body = file_data

                    # 拼接响应报文
                    response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                    # 发送数据
                    new_socket.send(response_data)
                else:
                    # 响应行
                    response_line = "HTTP/1.1 200 OK\r\n"
                    # 响应头
                    response_header = "Server: PWS1.0\r\n"

                    # 响应体
                    response_body = file_data

                    # 拼接响应报文
                    response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                    # 发送数据
                    new_socket.send(response_data)
                finally:
                    # 关闭服务与客户端的套接字
                    new_socket.close()
        else:
            logging.warning("客户端关闭了……")
            new_socket.close()
            return

    def start(self):
        """启动"""
        while True:
            # 等待接受客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            threading.Thread(target=self.handle_client_request, args=(new_socket, ip_port), daemon=True).start()


# 程序入口函数

def main():
    # 获取命令行参数判断长度

    if len(sys.argv) != 2:
        print("执行命令如下：python3 xxx.py 9000")
        return
        # 判断端口号是否是数字
    if not sys.argv[1].isdigit():
        print("执行命令如下：python3 xxx.py 9000")
        return
        # 需要转成int类型
    port = int(sys.argv[1])

    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动web服务器
    web_server.start()


if __name__ == '__main__':
    main()
