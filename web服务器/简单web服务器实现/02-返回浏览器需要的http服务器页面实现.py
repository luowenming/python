import socket
import re


def server_client(new_socket):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode("utf-8")
    #print(request)

    # 2. 返回http格式的数据，给浏览器
    # 2.1 准备返回的数据header
    response = "HTTP/1.1/ 200 OK\r\n"
    response += "\r\n"

    # 打开某个页面
    try:
        f = open("./html/index.html", "rb")
        html_content = f.read()
        f.close()
    except:
        print("文件打开失败！")
    
    # GET /index.html HTTP/1.1
    request_lines = request.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print(file_name)

    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)

    # 3. 关闭套接字
    new_socket.close()


def main():
    """用来完成整体控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)


    while True:

        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户服务
        server_client(new_socket)
    
    # 6. 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()