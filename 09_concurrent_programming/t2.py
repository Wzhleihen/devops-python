import  threading
import time
import logging

FORMAT = '%(asctime)s - %(threadName)s %(thread)d - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

class MyThread(threading.Thread):
    def start(self) -> None :  # 重写start方法
        print('start thread')
        super().start()  # 调用父类的start方法，创建线程，启动线程

    def run(self):  # 重写run方法
        print('run thread')  #用于跑函数
        super().run()  # 调用父类的run方法，执行线程


def worker():
    logging.info('working~~~~~~~~~~~~')
    time.sleep(2)
    logging.info('finished')
    
t = MyThread(target=worker, name='worker')
# t.start()


t.run()