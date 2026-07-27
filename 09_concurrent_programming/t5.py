import threading
import time
import logging

FORMAT = '%(asctime)s - %(threadName)s %(thread)d - %(levelname)s - %(message)s'
# 时间-线程名-线程id-日志级别-日志信息

logging.basicConfig(level=logging.INFO, format=FORMAT)

# x  = 0  # 全局变量，多个线程共享同一个全局变量，线程不安全

class A():
    def __init__(self):
        self.x = 0

# global_data = A()  # 能不能解决线程安全问题？
# 问题引入：全局变量，多个线程共享同一个全局变量，线程不安全，怎么解决

# 创建一个线程局部存储对象（Thread Local Storage）
# 整个进程只有一个 global_data 对象，
# 但每个线程都会拥有属于自己的属性字典，因此访问 global_data.x 时，
# 实际访问的是当前线程自己的 x，互不影响。
global_data = threading.local()

# 局部变量只能在当前函数里使用。
'''
这也是 Flask、Django 等 Web 框架为什么大量使用 threading.local()
（以及后来基于 contextvars 的上下文机制）的原因：
在同一个请求处理链中共享数据，而不必层层传递参数，同时又保证不同请求（不同线程）之间的数据彼此隔离。
'''


def worker():
    global_data.x = 0
    logging.info('Worker: starting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    # x = 0   # x 是局部变量，局部变量和每一次函数调用的栈帧有关，每次调用函数，都会创建新的栈帧，栈帧中保存了函数的局部变量
    # 如果多线程线程运行，使用的局部变量，那很安全，因为每个线程的栈帧都是独立的
    for i in range(1000):
        time.sleep(0.0001)
        global_data.x += 1    # 假如使用全局会一直往上加，因为多个线程共享同一个全局变量，线程不安全
    # logging.info(f"Worker: finishing x={x} thread={threading.current_thread().name}")
    
    # logging.info('finishing', x, threading.current_thread().name) #错误写法， logging.info(msg, *args) msg 是第一个参数，args 是后面的参数
    logging.info("Worker: finishing x=%d thread=%s",global_data.x,threading.current_thread().name) # 正确写法
    

for i in range(10):
    t1 = threading.Thread(target=worker, name=f"t-{i+1}")
    t1.start()

print('=' * 30)