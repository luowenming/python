name_list = ['张三','李四','王五','张三']
num_list = [6,2,4,1,10]

#del 关键字将变量从内存中删除后续代码就不能使用这个变量
#del name_list[0]

#name_list.pop(1) 删除指定索引的数据

#len 列表的长度
#list_len = len(name_list)

#list_len = name_list.count('张三')

#从列表中删除数据，remove删除出现第一次
#name_list.remove('张三')


#列表排序

#升序
#num_list.sort()

#降序
#num_list.sort(reverse=True)

#反转
#num_list.reverse()

#使用迭代
for my_name in name_list:
    print('我的名字叫：%s' % my_name)

#print(num_list)