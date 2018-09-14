import socket

    def main():
        #1,创建套接字
        udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        #2,绑定一个本地信息
        localaddr = ('',7788) #第一个参数ip，第二个参数端口
        udp_socket.bind(localaddr)

        #3,打印接收到的数据
        recv_data = udp_socket.recvfrom(1024)  # 1024是字节
        #解析收到的数据
        recv_msg = recv_data[0]  # 存储接收到的数据
        recv_addr = recv_data[1]  # 存储发送的地址信息
        print('%s:%s' % (str(recv_addr),recv_msg.decode('gbk')))  # 解码
        #4,关闭套接字
        udp_socket.close()

if __name__ == '__main__':
    main()