import datetime
import multiprocessing
import logging


FORMAT = '%(asctime)s - %(processName)s - %(threadName)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def calc():
    s =  0
    for i in range(100000000):  # 1亿次计算
        s += 1
    logging.info(s)


if __name__ == '__main__':
    start = datetime.datetime.now()
    ps = []
    for i in range(3):
        p = multiprocessing.Process(target=calc, name=f'p-{i}')
        ps.append(p)
        p.start()
    
        
    for p in ps:
        p.join()
        
    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)  # 计算密集型任务，串行