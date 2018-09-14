#len统计字符串长度
#count()在字符串中出现的次数
#index()某一个指定的元素在列表出现的位置


hello_str = 'hello world'
# #1,统计字符串的长度
# print(len(hello_str))
#
# #2,统计某一个字符串出现的次数
# print(hello_str.count('llo'))
# #如果字符串没有出现，则0
# print(hello_str.count('l'))
#
#
# #3，判断某一个字符串出现的位置
# print(hello_str.index('llo'))


# #1,判断是否以指定的字符串开始
# print(hello_str.startswith('hello'))
#
# #2,判断是否以指定的字符串结束
# print(hello_str.endswith('o'))
#
# #3,字符串的查找
# print(hello_str.find('llo'))
# #index方法同样可以，但是没有会报错，find()不存在返回-1
# print(hello_str.find('abc'))
#
# #4，替换字符串
# #方法执行完成之后，会完成一个新的字符串
# #不会修改原有字符串的内容
# print(hello_str.replace('world', 'python'))

#假定：一下内容是从网上抓取的
#要求：顺序并且居中对其
poem = ['登鹤雀楼',
        '黄志欢',
        '白日依山尽',
        '黄何日黑龙',
        '欲穷千里梦',
        '更上一层楼'
        ]
for poem_str in poem:
    print(poem_str.center(10))