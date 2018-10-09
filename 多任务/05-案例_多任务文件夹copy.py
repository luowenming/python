import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    #print('===>模拟copy文件：从%s----》到%s 文件名是:%s' % (old_folder_name, new_folder_name, file_name))

    old_f = open(old_folder_name + '/' + file_name, 'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + '/' + file_name, 'wb')
    new_f.write(content)
    new_f.close()

    # 往队列中写入数据
    q.put(file_name)

def main():
    # 1. 获取用户要copy的文件夹名字
    old_folder_name = input('请输入要copy的文件夹的名字：')

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + '[复件]'
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹里面所有待copy的文件名字 listdir()
    file_names = os.listdir(old_folder_name)
    #print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    #po.join()
    file_name_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        #print('文件copy完成：%s' % file_name)
        print('\r拷贝进度：%.2f%%' % (copy_ok_num*100 / file_name_num), end="")

        if copy_ok_num >= file_name_num:
            break
    print()

    # 6. 复制源文件中的文件，到新的文件夹中的文件去


if __name__ == "__main__":
    main()