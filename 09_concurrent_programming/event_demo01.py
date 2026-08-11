import logging
import time
import threading


FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

flag = False
event = threading.Event()  # 创建一个事件对象, 适合用于 1对n的通知

def boss():
    logging.info("I'am boss, watching U")
    # while True:
    #     time.sleep(1)
    #     if flag:
    #         break
    event.wait()  # 阻塞等待事件被设置
    logging.info("Good job")
        
def worker(count=10):
    global flag 
    logging.info("I'am worker, forwarding U")
    cpus = []
    # while True:
    while not event.wait(0.5):  # 阻塞等待事件
        time.sleep(0.2)
        cpus.append(1)
        if len(cpus) >= count:
            # flag = True
            event.set()  # 设置事件
            break
    logging.info(f"Finished, cups={len(cpus)}")


# w = threading.Thread(target=worker, name="worker")
# b1 = threading.Thread(target=boss, name="boss1")
# b2 = threading.Thread(target=boss, name="boss2")

w = threading.Thread(target=worker, name="worker", args=(event))
b1 = threading.Thread(target=boss, name="boss1", args=(event))
b2 = threading.Thread(target=boss, name="boss2", args=(event))

b1.start()
b2.start()
w.start()