import socket


# 要求1：最终代码效果可以使用with TcpSocket("s", "192.168.126.178", 8080) as socket:语句获取套接字socket；
#
# 要求2：TcpSocket类中：
# 第一个参数如果是"s"，创建服务端套接字，"192.168.126.178", 8080分别为要绑定的IP和端口号；
# 第一个参数如果是"c"，则创建客户端套接字，"192.168.126.178", 8080分别为要连接的服务端的IP和端口号；
#
# 要求3：如果创建服务端套接字，上下文中能自动绑定IP和端口号，且处于监听状态；
#
# 要求4：如果创建客户端套接字，上下文中能自动连接到目标服务端。
class TcpSocket(object):

    def __init__(self, server_or_client, host, port):
        if server_or_client not in "cs":
            raise Exception("您输入的参数有误（请输入c或者s）")
        self.__server_or_client = server_or_client
        self.__host = host
        self.__port = port

    def __enter__(self):
        if self.__server_or_client == "s":
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置端口复用
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SOCK_STREAM)
            server_socket.bind((self.__host, self.__port))
            server_socket.listen(128)
            self.__server_socket = server_socket
            return server_socket
        else:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.__host, self.__port))
            self.__client_socket = client_socket
            return client_socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__server_or_client == "c":
            self.__client_socket.close()
        else:
            self.__server_socket.close()
