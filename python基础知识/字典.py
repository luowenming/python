#len(字典) 获取字典的键值对数量
#字典.keys()所有列表key
#字典.value()所有列表value
#字典.items()所有列表的（key,value）

xiaoming = {'name' : '小明',
            'age' : 18}

# #1,取值
# print(xiaoming['name'])
#
# #2,增加/修改
# #如果key不存在，就新增。否则就修改
# xiaoming['height'] = 1.75
#
# #3,删除
# xiaoming.pop('name')

# #1,统计键值对数量
# print(len(xiaoming))
#
# #2,合并字典
# temp = {'height' : 1.75}
# xiaoming.update(temp)
#
# #3清空字典
# xiaoming.clear()

#4 遍历字典
#k是每一次循环获取的key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))


print(xiaoming)