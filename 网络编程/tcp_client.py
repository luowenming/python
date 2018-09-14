import socket

def main():
    # 1，创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2，链接服务器
    dest_ip = input("请输入要链接服务器的ip：")
    dest_port = int(input("请输入要链接服务器的port："))
    localaddr = (dest_ip, dest_port)
    # 3，收发数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.connect(send_data.encode('gbk'))
    # 4，关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main():