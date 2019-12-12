import socket

# 创建tcp服务端套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定端口
server.bind(("", 9090))
# 设置监听
server.listen(123)
# 等待客户端请求
new_socket, ip_port = server.accept()

while 1:
    # 接受请求数据
    recv_client_data = new_socket.recv(4096)
    if len(recv_client_data) == 0:
        print("客户关闭请求了")
        # 关闭服务与客户端的套接字
        break
    # 对二进制数据进行解码
    recv_client_content = recv_client_data.decode('utf-8')
    print(recv_client_content)
    new_socket.send("我很好".encode("utf-8"))

new_socket.close()
server.close()
