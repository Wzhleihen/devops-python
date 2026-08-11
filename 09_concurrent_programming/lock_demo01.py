import threading 
import logging

FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

lock = threading.Lock()

# 锁的简单使用
# print(lock.locked())  # False 未获取锁
# print(lock.acquire())  # True 获取锁
# print(lock.locked())  # True 获取锁
# print(lock.release())  # 释放锁  # 返回None
# print(lock.locked())  # False 未获取锁

def worker():
    logging.info('working~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    lock.acquire()  # 获取锁
    logging.info('end ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


for i in range(5):
    threading.Thread(target=worker, name=f'thread-{i}', daemon=True).start()

while True:
    cmd = input('>>>')
    if cmd == 'r':
        lock.release()  # 释放锁
        print('release one time')
    elif cmd == 'quit':
        break
    else:
        print(threading.enumerate())  # 获取当前所有线程
        print(lock.locked())  # 获取锁状态