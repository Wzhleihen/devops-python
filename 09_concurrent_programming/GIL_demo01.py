import logging
import datetime

logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")

start = datetime.datetime.now()


# 计算密集型任务
def calc():
    sum = 0
    for i in range(1000000000):  # 10亿次计算
        sum += 1
    print(sum)


calc()
calc()
calc()
calc()


delta = (datetime.datetime.now() - start).total_seconds()

logging.info(delta)  # 计算密集型任务，串行

'''
运行结果： cpu: i5-1240p 12核 16线程 32GB 内存

1000000000
1000000000
1000000000
1000000000
27328 122.03044
'''
