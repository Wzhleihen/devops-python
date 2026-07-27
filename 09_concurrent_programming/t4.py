import threading
import time
import sys

def worker(x=1,f = sys.stdout, n=10):
    print('worker start', file=f)
    for i in range(n):
        time.sleep(1)
        # print('#' * 30, file=f)
        print(f'{x}' * 30,  {i}, file=f)
    print('worker end', file=f)


t1 = threading.Thread(target=worker, name='worker1',daemon=True)
t1.start()
t1.join()  # 等待线程t1执行完毕再继续往下执行
# t2 = threading.Thread(target=worker, name='worker2',daemon=False, args=(2, sys.stderr, 5))
# t2.start()
# # time.sleep(5)

# t3 = threading.Thread(target=worker, name='worker3',daemon=True, args=(3, sys.stdout, 10))
# t3.start()

# print(threading.main_thread().daemon)  # 主线程是 not-daemon 线程
print('main thread')

