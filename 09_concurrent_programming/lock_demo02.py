import threading 
import logging
import time

FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

lock = threading.Lock()

# 10个工人同时生成1000个杯子，老板来监督

cups = []
lock = threading.Lock()

def worker(count=1000):
    logging.info("I'm working")
    while True:
        lock.acquire()  # 获取锁
        if len(cups) >= count:
            lock.release()  # 释放锁 位置1  在break之前释放锁，其他线程可以获取锁，程序不会卡死, 但是数据量是完成
            break
        # lock.release()  # 释放锁 位置2 在
        time.sleep(0.0001) #为了看出线程切换效果,模拟杯子制作时间
        cups.append(1)
        lock.release()  # 释放锁 位置3 对 在这个位置，数据量是完成，但是程序运行到这里会产生死锁，因为在break之前没有释放锁，导致其他线程无法获取锁，程序卡死
    # 这三个位置，释放锁有什么区别？能不能完成老板的任务？
    logging.info('I finished my job. cups={}'.format(len(cups)))

for i in range(1, 11):
    t = threading.Thread(target=worker, name="w{}".format(i), args=(1000,))
    t.start()

''' 
2026-08-09 21:23:14,879 - w2 - INFO - I finished my job. cups=1000
2026-08-09 21:23:14,879 - w9 - INFO - I finished my job. cups=1001
2026-08-09 21:23:14,879 - w6 - INFO - I finished my job. cups=1002
2026-08-09 21:23:14,879 - w3 - INFO - I finished my job. cups=1003
2026-08-09 21:23:14,879 - w8 - INFO - I finished my job. cups=1004
2026-08-09 21:23:14,879 - w1 - INFO - I finished my job. cups=1005
2026-08-09 21:23:14,879 - w5 - INFO - I finished my job. cups=1006
2026-08-09 21:23:14,879 - w10 - INFO - I finished my job. cups=1007
2026-08-09 21:23:14,880 - w4 - INFO - I finished my job. cups=1008
2026-08-09 21:23:14,880 - w7 - INFO - I finished my job. cups=1009
'''