import socket
import threading


class HttpWebService(object):

    def __init__(self, port):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        socket_server.bind(("", port))
        socket_server.listen(128)
        self.server = socket_server

    def start(self):
        """启动服务"""
        print("服务器启动了")
        while 1:
            new_socket, ip_port = self.server.accept()
            print("建立新的连接：", ip_port)
            threading.Thread(target=self.handle_request, args=(new_socket,), daemon=True).start()

    def handle_request(self, new_socket):
        """处理请求"""
        while 1:
            client_data = new_socket.recv(1024)
            if len(client_data) == 0:
                print('客户端关闭了……')
                new_socket.close()
                return
            client_content = client_data.decode("utf-8")
            print("接收到数据：", client_content)
            new_socket.send("我收到数据了".encode("utf-8"))


if __name__ == '__main__':
    HttpWebService(9090).start()
