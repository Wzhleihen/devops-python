import socket
import threading
import logging


FORMAT = '%(asctime)s - %(processName)s - %(threadName)s - %(module)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

class Chatserver:
    def __init__(self, host='127.0.0.1', port=9999):
        self.addr = (host, port)   # 定义服务端地址
        self.sock = socket.socket()  # 创建套接字
        self.event = threading.Event()   # 用于线程间通信，控制线程退出
        self.clients = {}   # 存储已连接的客户端
        self.lock = threading.Lock()   # 解决线程间数据安全问题，防止多个线程同时修改 clients 字典

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen(5)
        
        # 开启一个线程，专门用于接收客户端连接，避免阻塞主线程
        threading.Thread(target=self.accept, name='server_accept').start() 
    
    def accept(self):
        # 监听客户端连接，当有客户端连接时，创建一个线程，用于接收客户端消息
        count = 1
        while not self.event.is_set():
            network, addr = self.sock.accept()
            f = network.makefile('rw')
            with self.lock:
                self.clients[addr] = f, network
            logging.info(f'{network} {addr}')
            threading.Thread(target=self.recv, args=(f, addr), name=f'r-{count}-{addr}').start()
            count += 1
    
    def recv(self, f, addr):
        while not self.event.is_set(): 
            try:
                # data = f.read(1024)
                data = f.readline().strip()  # 读取一行数据，去掉换行符
            except Exception as e:
                logging.error(e)
                break
            if data == b'' or data == b'quit':
                with self.lock:
                    _, sock = self.clients.pop(addr)
                logging.info(f'{addr} bye')
                sock.close()
                f.close()
                break
            # msg = f'form {*addr}: {data.decode()}'
            msg = 'form {} : {} data={}'.format(*addr, data)
            logging.info(msg)
            # logging.info(f'{network} {addr}')
            # 在这里加入 lock
            with self.lock:
                # for c in self.clients.values():
                #     c.send(msg.encode())
                for ff, _ in self.clients.values():
                    ff.write(msg + '\n')
                    ff.flush()  # 刷新缓冲区，确保数据发送出去
                    
    def stop(self):
        self.event.set()
        with self.lock:
            # for c in self.clients.values():
            #     c.close()
            for f,s in self.clients.values():
                f.close()
                s.close()
        self.sock.close()

if __name__ == '__main__':
    cs = Chatserver()
    cs.start()
    print(threading.enumerate())
    # print('~~~ * 30')