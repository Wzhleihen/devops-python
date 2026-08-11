import datetime
import time
import multiprocessing
import logging
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait
import threading



FORMAT = '%(asctime)s - %(processName)s - %(threadName)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def calc():
    s =  0
    for i in range(100000000):  # 1亿次计算
        s += 1
    logging.info(s)
    return s

start = datetime.datetime.now()
# executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix='test-calc')  # 创建线程池，最大线程数3, 线程名称前缀 test-calc
# [<_MainThread(MainThread, started 2020)>, <Thread(test-calc_0, started 41952)>, <Thread(test-calc_1, started 26476)>, <Thread(test-calc_2, started 45200)>]

fs = []
with  ThreadPoolExecutor(max_workers=3, thread_name_prefix='test-calc') as executor:
    for i in range(3):
        future = executor.submit(calc)  # 提交任务到线程池
        fs.append(future)

# wait(fs)  # 阻塞到所有任务完成

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)  # 计算密集型任务，串行

# 获取最终结果返回值
for f in fs:
    print(f.result())


# while True:
#     time.sleep(1)
#     print(threading.enumerate()) # 获取当前所有线程
