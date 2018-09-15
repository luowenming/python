import socket

def send_file_to_client(new_client_scoket, client_addr):
    # 1.接收客户端需要下载的文件名
    # 接收客户端发送过来的文件名
    file_name = new_client_scoket.recv(1024).decode('gbk')
    print("客户端%s需要下载的文件名是：%s" % (str(client_addr), file_name))

    file_content = None
    # 2.打开这个文件读取数据
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件（%s）" % file_name)

    # 3.发送文件的数据给客户端
    # 发送文件的数据给客户端
    if file_content:
        new_client_scoket.send(file_content)


def main():
    # 1，买个手机（创建套接字socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2，插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("", 7890))

    # 3，将手机设置为正常的响玲状态（让默认的套接字由本地变为被动 listen）
    tcp_server_socket.listen(128)

    print('---1---')
    # 4，等待别人的电话到来（等待客户端的链接 accept）
    new_client_scoket, client_addr = tcp_server_socket.accept()
    print('---2---')
    print(client_addr)

    # 5. 调用发送文件函数，完成为客户端服务
    send_file_to_client(new_client_scoket, client_addr)

    # 关闭套接字
    new_client_scoket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()