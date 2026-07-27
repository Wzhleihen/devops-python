import threading
import time
import sys

def worker(x=1,f = sys.stdout):
    print('worker start', file=f)
    for i in range(10):
        time.sleep(0.5)
        # print('#' * 30, file=f)
        print(f'{x}' * 30, file=f)
    print('worker end', file=f)


t1 = threading.Thread(target=worker, name='worker1')
t1.start()
t2 = threading.Thread(target=worker, name='worker2', kwargs={'x': 2, 'f': sys.stderr})
t2.start()
print('main thread')

