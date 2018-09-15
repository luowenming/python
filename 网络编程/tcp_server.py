import socket

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

    # 接收客户端发送过来请求
    recv_data = new_client_scoket.recv(1024)
    print(recv_data)

    # 发送数据
    new_client_scoket.send("hahaha---ok-----".encode('gbk'))

    # 关闭套接字
    new_client_scoket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()