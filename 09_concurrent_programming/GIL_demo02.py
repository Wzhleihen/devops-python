import threading
import logging
import datetime

FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


start = datetime.datetime.now()


# 计算密集型任务
def calc():
    total = 0
    for i in range(1000000000):  # 10亿次计算
        total += 1
    logging.info(total)


t1 = threading.Thread(target=calc)
t2 = threading.Thread(target=calc)
t3 = threading.Thread(target=calc)
t4 = threading.Thread(target=calc)


t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()


delta = (datetime.datetime.now() - start).total_seconds()

logging.info(delta)

'''
运行结果： cpu: i5-1240p 12核 16线程 32GB 内存
2026-08-10 22:42:38,614 - Thread-1 (calc) - INFO - 1000000000
2026-08-10 22:42:39,251 - Thread-4 (calc) - INFO - 1000000000
2026-08-10 22:42:39,902 - Thread-2 (calc) - INFO - 1000000000
2026-08-10 22:42:40,634 - Thread-3 (calc) - INFO - 1000000000
2026-08-10 22:42:40,635 - MainThread - INFO - 117.519599

因为存在GIL（全局解释器锁），所以多线程在计算密集型任务中并不能提高性能，反而会因为线程切换带来额外的开销，导致性能下降。
怎么解决GIL问题？使用多进程（multiprocessing）来替代多线程（threading），因为每个进程都有自己的Python解释器和内存空间，所以不会受到GIL的影响。
'''
