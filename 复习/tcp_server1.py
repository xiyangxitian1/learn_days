import socket
import threading


def handle_rq(new_socket):
    while 1:
        recv_data = new_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode("gbk")
            print(recv_content)

            resp_line = "HTTP/1.1 200 OK \r\n"
            resp_header = "Server: PWS2.0 \r\n"
            data = ""
            with open("static/index.html", 'rb') as f:
                data = f.read()
            resp_body = data
            resp_data = (resp_line + resp_header + "\r\n").encode('utf-8') + resp_body
            # new_socket.send("发送的数据:我收到了".encode("gbk"))
            new_socket.send(resp_data)
        else:
            print("连接关闭了……")
            break
    new_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("", 9090))
    server_socket.listen(128)

    while 1:
        new_socket, ip_port = server_socket.accept()
        print("连接成功：", ip_port)
        threading.Thread(target=handle_rq, args=(new_socket,), daemon=True).start()
