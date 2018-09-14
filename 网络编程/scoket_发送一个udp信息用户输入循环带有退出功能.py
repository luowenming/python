import socket

def main():
    #创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #可以使用套接字收发数据
    #udp_socket.send(b"hahahaha",("对方的ip",端口))
    while True:
        send_data = input("请输入要发送的数据：")
        if send_data == 'exit':
            break
        udp_socket.sendto(send_data.encode('utf-8'),("192.168.0.163",8080))

    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
