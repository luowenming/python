import socket

def main():
    #创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #可以使用套接字收发数据
    #udp_socket.send(b"hahahaha",("对方的ip",端口))
    udp_socket.sendto(b"hahahaha",("192.168.0.163",8080))

    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
