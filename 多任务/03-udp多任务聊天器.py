import socket
import threading

def recv_data(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input('请输入要发送的数据：')
        send_msg = udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('', 7890))

    dest_ip = input('请输入对方的ip：')
    dest_port = int(input('请输入对方的端口：'))


    # 创建多线程
    t1 = threading.Thread(target=recv_data, args=(udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()