#不能修改其内容  tuple
#运用场景
#1，函数的返回值或者参数
#2,格式化字符串
info = ('zs',18)
print('%s的年龄是：%d' % info)

info_str = '%s的年龄是：%d' % info

print(info_str)


#元祖有两个方法
#count()  index()

#取索引
info_tuple = ('zhangsan',18,1.75,18)
print(info_tuple[0])
print(info_tuple.index('zhangsan'))

#统计计数
print(info_tuple.count(18))

#len
print(len(info_tuple))