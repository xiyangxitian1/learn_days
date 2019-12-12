import socket
import time

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect(("localhost", 9090))

while 1:
    # data1 = input("请输入要发给服务器的信息(q结束)：")
    time.sleep(2)
    data1 = "你好"
    if data1 == "q":
        break
    client_server.send(data1.encode("utf-8"))
    data = client_server.recv(4096)
    if len(data) == 0:
        print("服务器挂了")
        client_server.close()
        break
    print(data.decode("utf-8"))

client_server.close()
