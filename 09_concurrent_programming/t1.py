# 线程基础
import  threading
import time

def worker():
    print('working~~~~~~~~~~~~')
    # while True:
    for i in range(10):
        time.sleep(1)
        print('=' * 30)
        if i > 4:
            # break
            return  # 线程结束，线程对象t.is_alive()返回False
    print('finished')
    
def add(x, y):
    worker()
    print('-' * 30)
    return x + y  # 目前情况下，返回值由于当前库，无法获取到，在某些情况下，线程的返回值可以通过queue队列来获取到

t = threading.Thread(target=add, name='add', args=(1, 2))  # 创建线程对象

t.start()  # 启动线程  系统调用，创建操作系统线程，启动运行target函数


# worker()  #只是一个普通函数，它不会创建线程；它在哪个线程中执行，完全取决于是谁调用了它
# 当前线程创建一个新的函数栈帧，执行完后返回，不会创建新线程

