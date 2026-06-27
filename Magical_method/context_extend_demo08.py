from contextlib import contextmanager

import time
import datetime

def add(x, y):
    time.sleep(2)
    return x + y

@contextmanager
def timeit(fn):  # 用函数实现上下文管理，此函数只能yield 一下
    print('之前增强')
    start = datetime.datetime.now()
    try:
        yield fn
    finally:
        print('之后增强')
        delta = (datetime.datetime.now() - start).total_seconds()
        print(add.__name__ , delta)

with timeit(add) as t:
    # print(t)
    # print('with start')
    # 1/0
    # print('with end')
    add(4,5)