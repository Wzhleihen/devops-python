import time

from Magical_method import test01

# with open('test') as f:
#     pass


# class A:
#     def __init__(self):
#         print(1, 'init ~~~')
#         time.sleep(2)
#
#     def __enter__(self):
#         print(2, 'enter ~~~')
#         time.sleep(2)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(3, 'exit ~~~')
#         time.sleep(2)
#
# with A() as a:
#     print(4, 'with start~~~')
#     # 1/0
#     time.sleep(2)
#     print(5, 'with end~~~')
#
# # 上下文管理（Context Manager）语法。
# f1 = open('test01.py')  # 方法里面已经内置封装了 is 和 == ，即 __eq__ 和 __ne__ 用法
# with f1 as f2:
#     print(f1 == f2)  # True
#     print(f1 is f2) # True

#
# class A:
#     def __init__(self):
#         print(1, 'init ~~~')
#
#
#     def __enter__(self):
#         print(2, 'enter ~~~')
#         return  self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)  # 异常类型
#         print('---' * 10)
#         print(exc_val)  # 异常值
#         print('---' * 10)
#         print(exc_tb)  # 异常对象
#         print('---' * 10)
#         print(3, 'exit ~~~')
#         # return 111  # return 值如果等价于 True，则表示异常被处理了，程序继续往下执行，否则程序会抛出异常
#
# t1 = A()
# with t1 as t2:
#     print(4, 'with start~~~')
#     1/0
#     print(t2 , '????????')
#     print(t1 == t2)  # ?
#     print(t1 is t2)
#     print(5, 'with end~~~')

import time
import datetime

def add(x ,y):
    time.sleep(2)
    return  x + y

class A():
    def __init__(self):
        print(1, 'init ~~~')

    def __enter__(self):
        print(2, 'enter ~~~')
        self.start = datetime.datetime.now()
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(3, 'exit ~~~')
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print(f'took {delta}s')

with A() as a:
    print(4, 'with start~~~')
    add(1, 2)
    print(5, 'with end~~~')