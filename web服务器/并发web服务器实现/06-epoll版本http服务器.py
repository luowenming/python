import socket
import re
import gevent
from gevent import monkey
import select

monkey.patch_all()

def server_client(new_socket, request):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    #request = new_socket.recv(1024).decode("utf-8")
    #print(request)

    # 打开某个页面
    try:
        f = open("./html/index.html", "rb")
        html_content = f.read()
        f.close()
    except:
        print("文件打开失败！")

    # 2. 返回http格式的数据，给浏览器
    # 2.1 准备返回的数据header
    response = "HTTP/1.1/ 200 OK\r\n"
    response += "Content-Length:%d\r\n" % (len(html_content))
    response += "\r\n"

    # GET /index.html HTTP/1.1
    request_lines = request.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print(file_name)

    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)

    # 3. 关闭套接字
    #new_socket.close()


def main():
    """用来完成整体控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False) # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:

        fd_event_list = epl.poll() # 默认堵塞，直到os检测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞
        # [(fd, event)]

        for fd, event in fd_event_list:
            # 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    server_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

        # 5. 为这个客户服务
        # 开一个协程为这个客户服务
        #gevent.spawn(server_client, new_socket)

        #子线程会共享主进程的资源，所有不需要关闭
        #new_socket.close()
    
    # 6. 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()