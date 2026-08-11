import threading
from threading import Thread, Lock
import time
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

cups = []
lock = Lock() #锁

def worker(count=1000):
    logging.info("I'm working")
    while True:
        with lock: #获取锁,离开with释放锁
            if len(cups) >= count:
                logging.info('leaving')
                break
            time.sleep(0.0001) #为了看出线程切换效果,模拟杯子制作时间
            cups.append(1)
            logging.info(lock.locked())  #查看锁是否被占用
    logging.info('I finished my job. cups={}'.format(len(cups)))

for i in range(1, 11):
    t = Thread(target=worker, name="w{}".format(i), args=(1000,))
    t.start()