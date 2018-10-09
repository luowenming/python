class Fobonacci(object):
    def __init__(self, all_num):
        self.names = list()
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.current_num = 0

        
    def __iter__(self):
        """如果想要一个对象成为一个可以迭代的对象，既可以使用for，那么必须实现__iter__方法，__trer__方法必须返回return __next__方法"""
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fobonacci(10)

for temp in fibo:
    print(temp)