import socket
import logging
import threading
import datetime

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.event = threading.Event()  # 用于线程间通信，控制线程退出
        
    def start(self):
        self.sock.connect(self.addr)
        self.send("I'm ready")
        
        # 开启一个线程，专门用于接收服务端消息，避免阻塞主线程
        threading.Thread(target=self.recv, name='client_recv').start()
    
    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as e:
                logging.error(e)
                break
            
            msg = "{:%Y-%m-%d %H:%M:%S} {}:\n{}\n{}\n ".format(
                datetime.datetime.now(), 
                *self.addr, 
                data.strip()
                )
            
            logging.info(msg)
            
    def send(self, msg: str):
        data = "{}\n".format(msg.strip()).encode() # 消息末尾添加换行符，用于服务端按行读取
        self.sock.send(data)
    
    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info('Client stops.')
    

def main():
    client = ChatClient()
    client.start()
    
    while True:
        msg = input('>>> ')
        if msg.strip() == 'quit':
            break
        client.send(msg)
    
    client.stop()


if __name__ == '__main__':
    main()
        
        