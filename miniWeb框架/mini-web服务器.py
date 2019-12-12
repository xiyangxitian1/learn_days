import socket
import threading
import sys
import framework_class as framework
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename="log.txt",
                    filemode="w"
                    )

logging.debug("开启日志了……")


class HttpWebService(object):

    def __init__(self, port):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        socket_server.bind(("", port))
        socket_server.listen(128)
        self.server = socket_server

    def start(self):
        """启动服务"""
        logging.info("服务器启动了")
        while 1:
            new_socket, ip_port = self.server.accept()
            # print("建立新的连接：", ip_port)
            logging.info("建立新的连接的请求ip与端口号：" + str(ip_port))
            threading.Thread(target=HttpWebService.handle_request, args=(new_socket, ip_port), daemon=True).start()

    @staticmethod
    def handle_request(new_socket, ip_port):
        """处理请求"""
        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            # print("关闭浏览器了")
            logging.warning("与{}断开连接了".format(ip_port))
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_client_content = recv_client_data.decode("utf-8")
        # print(recv_client_content)
        # 根据指定字符串进行分割， 最大分割次数指定2
        request_list = recv_client_content.split(maxsplit=2)

        # 获取请求资源路径
        request_path = request_list[1]
        # print(request_path)

        # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
        if request_path == "/":
            request_path = "/index.html"

        logging.info("收到请求：" + request_path)

        if request_path.endswith(".html"):
            """处理动态请求"""
            # response_data = framework.handle_req(request_path)
            response_data = framework.FrameWork().handle_req(request_path)
            # 发送数据
            new_socket.send(response_data)
            # 关闭服务与客户端的套接字
            new_socket.close()
        else:
            """下面是处理静态请求"""
            try:
                # 动态打开指定文件
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception as e:
                # 请求资源不存在，返回404数据
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
            else:
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
            finally:
                # 响应头
                response_header = "Server: PWS1.0\r\n"
                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
                # 关闭服务与客户端的套接字
                new_socket.close()

    @staticmethod
    def handle_request_keep_alive(new_socket):
        """处理请求(上面的是一次连接，这个要保持连接)"""
        while 1:
            # 代码执行到此，说明连接建立成功
            recv_client_data = new_socket.recv(4096)
            if len(recv_client_data) == 0:
                print("关闭浏览器了")
                new_socket.close()
                return
            # 对二进制数据进行解码
            recv_client_content = recv_client_data.decode("utf-8")
            # print(recv_client_content)
            # 根据指定字符串进行分割， 最大分割次数指定2
            request_list = recv_client_content.split(maxsplit=2)
            # 获取请求资源路径
            request_path = request_list[1]
            # print(request_path)
            # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
            if request_path == "/":
                request_path = "/index.html"
            try:
                # 动态打开指定文件
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception as e:
                # 请求资源不存在，返回404数据
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
            else:
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
            finally:
                # 响应头
                response_header = "Server: PWS1.0\r\n"
                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
                # 关闭服务与客户端的套接字
                # new_socket.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("请求参数不正确！")
    else:
        port = sys.argv[1]
        if not port.isdigit():
            print("端口号只能是数字！")
        else:
            port = int(port)
            HttpWebService(port).start()
