# 线程基础
import  threading
import time

# 定义线程类，继承自threading.Thread类
class MyThread(threading.Thread):
    def start(self) -> None :  # 重写start方法
        print('start thread')
        super().start()  # 调用父类的start方法，创建线程，启动线程

    def run(self):  # 重写run方法
        print('run thread')  #用于跑函数
        super().run()  # 调用父类的run方法，执行线程

# def showreadinfo():
#     print(threading.main_thread(), threading.current_thread(), threading.active_count())  # 获取主线程对象，当前线程对象，当前活动线程数
#     # <_MainThread(MainThread, started 20296)> <_MainThread(MainThread, started 20296)> 1

def worker():
    print('working~~~~~~~~~~~~')
    # showreadinfo()
    # while True:
    for i in range(10):
        time.sleep(0.5)
        print('=' * 30)
        if i > 4:
            # break
            return          # 线程结束，线程对象t.is_alive()返回False
    print('finished')
    
# def add(x, y):
#     worker()
#     print('-' * 30)
#     return x + y  # 目前情况下，返回值由于当前库，无法获取到，在某些情况下，线程的返回值可以通过queue队列来获取到

# 在python线程中，是没有优先级的，线程的优先级是由操作系统来决定的
t = MyThread(target=worker, name='worker')  # 创建线程对象

# showreadinfo()  # 获取主线程对象，当前线程对象，当前活动线程数
# time.sleep(1)

# t.start()  # 启动线程  系统调用，创建操作系统线程，启动运行target函数 ， 只能运行一回

# x = threading.main_thread()  # 获取主线程对象
# print(type(x), x)  # <class '_MainThread'> <_MainThread(MainThread, started 20296)>

# print(x.name, x.ident, x.is_alive())  # MainThread 20296 True

# worker()  #只是一个普通函数，它不会创建线程；它在哪个线程中执行，完全取决于是谁调用了它
# 当前线程创建一个新的函数栈帧，执行完后返回，不会创建新线程

# while True:
#     time.sleep(1)
#     if t.is_alive():
#         print(threading.active_count(), threading.enumerate()) # 获取当前活动线程数，获取当前活动线程对象列表
    
#     if threading.active_count() == 1:  # 当前活动线程数为1，说明主线程是唯一的活动线程，其他线程都结束了
#         print('I will restart t')
#         t.start() # 线程对象t.is_alive()返回False，说明线程已经结束了，线程对象t可以重新启动


t.start()  # 启动线程  系统调用，创建操作系统线程，启动运行target函数 ， 只能运行一回
print('-*' * 30)  # start 的本质，创建线程对象，创建结束到主线程执行print 当前语句，再到其他线程执行target函数，中间有延迟

t.start() 

