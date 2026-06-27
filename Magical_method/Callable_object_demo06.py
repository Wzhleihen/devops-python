# def foo(a):
#     print('foo called', a)
#
# foo(1)
# #  等价于
# foo.__call__(2)
# print(callable(foo))
#
# # callable() 用来判断对象是否可调用

# class A:
#     def __call__(self, *args, **kwargs):
#         print(self, args, kwargs)
#
#
# print(callable(A()))
#
# t = A()
# t(1,2, a=3)
# t.__call__(1,2, x=3, y=6)
#
# # 不是来说类的，它指的是实例是不是可调用对象？类本身是可调用对象，对不对？分清楚了啊，

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         return  str(self)
#
#     def __repr__(self):
#         return f'<{__class__.__name__}, {self.x}, {self.y}>'
#
# t = Point(1,2)
# print(t())
# print(t)


# class Adder:
#     def __call__(self, *args):
#         self.result = sum(args)
#         # 更复杂，可以使用 reduce
#         return self.result
# adder = Adder()
# print(adder(*range(10)))
# print(adder.result)


# 定义一个斐波那契数列的类，方便调用，计算第n项。
# 增加迭代数列的方法、返回数列长度、支持索引查找数列项的方法

class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __repr__(self):
        return str(self.items)

    # 等价于上面
    # def __str__(self):
    #     return str(self.items)
    # __repr__ = __str__  # str(f), [f] f.__repr__() f.__str__()
    # 在很多类中，都是这样子写的

    def __len__(self):
        return len(self.items)
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError('index out of range')
        # if index >= len(self.items):
        print('-'* 30)  # 用于判断计算次数
        for i in range(len(self.items), index + 1):
            self.items.append(self.items[i-1] + self.items[i-2])

        return self.items[index]

    # def __call__(self, index):  # f(3) ==> f.__call__(3)
    #     return self[index]  # self.__getitem__(index)
    __call__ = __getitem__  # 等价于上面


f = Fib()
print(f)
print(f[3])  # 当函数被索引的时候，会调用__getitem__方法
print(f(3))  # 与上面不一样，这里是当函数被调用的时候，会调用__call__方法
print('+' * 30)
for x in f:
    print(x)
print(len(f))
print(f[11])

