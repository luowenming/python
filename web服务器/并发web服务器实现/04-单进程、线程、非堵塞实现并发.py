import socket
import time


tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("",7890))
tcp_server.listen(128)
tcp_server.setblocking(False) # 设置套接字为非堵塞方式

client_socket_list = list()

while True:
    time.sleep(1)
    try:
        new_socket, new_addr = tcp_server.accept()
    except Exception as ret:
        print("--没有新的客户端到来--")
    else:
        print("--只要没有产生异常，那么意味着 来了一个新的客户端--")
        new_socket.setblocking(False) # 设置套接字为非堵塞方式
        client_socket_list.append(new_socket)
    
    for client_cocket in client_socket_list:
        try:
            recv_data = client_cocket.recv(1024)
        except Exception as ret:
            print("--这个客户端没有发送过来数据--")
        else:
            if recv_data:
                # 对放发送过来了数据
                print("--对方发送过来了数据--", recv_data)
            else:
                # 对方调用了close recv返回
                client_socket_list.remove(client_cocket)
                client_cocket.close()
                print("--客户端已关闭--")
