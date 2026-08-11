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

if __name__ == '__main__':
    start = datetime.datetime.now()
    # executor = ProcessPoolExecutor(max_workers=3, )  # 创建进程池，最大进程数3
    fs = []
    with ProcessPoolExecutor(max_workers=6, ) as executor:
        for i in range(3):
            future = executor.submit(calc) 
            fs.append(future)

    # wait(fs)  # 阻塞到所有任务完成

    # for f in fs:
    #     print(f, f.done(),f.result())  # done不阻塞，result阻塞

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)  