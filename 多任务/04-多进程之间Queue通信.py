import multiprocessing


def download_form_web(q):
    """下载数据"""
    # 1, 模拟从网上下载数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print('---下载器从网上下载数据完毕---')


def analysis_data(q):
    """处理数据"""
    waitting_analysis_data = list()
    #  从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break
    print('---处理数据完毕：%s---' % waitting_analysis_data)

def main():
    # 1，创建一个队列
    q = multiprocessing.Queue()

    # 2，创建多个进程
    p1 = multiprocessing.Process(target=download_form_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()