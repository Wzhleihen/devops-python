import multiprocessing
import datetime
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(process)s %(message)s"
)


# CPU密集型任务
def calc():
    total = 0

    for _ in range(1000000000):
        total += 1
    logging.info(total)

if __name__ == "__main__":

    start = datetime.datetime.now()


    p1 = multiprocessing.Process(target=calc)
    p2 = multiprocessing.Process(target=calc)
    p3 = multiprocessing.Process(target=calc)
    p4 = multiprocessing.Process(target=calc)


    p1.start()
    p2.start()
    p3.start()
    p4.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()


    delta = (
        datetime.datetime.now() - start
    ).total_seconds()


    logging.info(delta)

''' 
使用多进程（multiprocessing）来替代多线程（threading），因为每个进程都有自己的Python解释器和内存空间，所以不会受到GIL的影响。效率提高了。
2664 1000000000
45900 1000000000
46468 1000000000
46272 1000000000
36340 46.835713
'''