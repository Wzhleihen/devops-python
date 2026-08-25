import socket
import selectors


server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen(5)  # 开始监听，最大连接数为5

# 建议所以IO对象都设置为非阻塞模式
""" 
原因： 如果设置为阻塞模式，那么在调用IO对象时，如果当前IO对象没有准备好，那么程序就会阻塞在这里，无法执行后续代码
"""
server.setblocking(False) # 设置为非阻塞模式

def accept(sock):
    network, raddr = sock.accept()  # 接第二阶段，处理IO对象的事件
    print(network, raddr)  # 打印客户端socket对象以及客户端地址
    network.send(b'hello')  # 给客户端发送数据
    network.setblocking(False)  # 设置为非阻塞模式
    selector.register(network, selectors.EVENT_READ, recv)  # 注册IO对象到selector中，关注读事件

def recv(sock):
    # 处理客户端发送的数据
    data = sock.recv(1024)
    print(data, '++++++++')  # 打印客户端发送的数据

selector = selectors.DefaultSelector()  # 默认选择对应操作系统最优的IO多路复用技术
key  = selector.register(server, selectors.EVENT_READ, accept)  # 注册IO对象到selector中，关注读事件
print(key)  # 打印key对象，key对象中包含了IO对象、关注的事件、以及附加数据

while True:
    events = selector.select()  # 开始监听IO对象，返回发生事件的IO对象列表，第一阶段
    print(events)  # 打印发生事件的IO对象
    for key, mask in events:
        key.data(key.fileobj)  # 调用附加数据，处理IO对象的事件
        
        
        # print(key, mask)  # 打印发生事件的IO对象以及事件类型
        # if key.data == 1234:
        #     network, raddr =key.fileobj.accept()  # 接第二阶段，处理IO对象的事件
        #     # print(network, raddr)  # 打印客户端socket对象以及客户端地址
        #     # network.send(b'hello')  # 给客户端发送数据
        #     network.setblocking(False)  # 设置为非阻塞模式
        #     selector.register(network, selectors.EVENT_READ, data=2233)  # 注册IO对象到selector中，关注读事件
        # if key.data == 2233:
        #     # 处理客户端发送的数据
        #     data = key.fileobj.recv(1024)
        #     print(data, '++++++++')

""" 
SelectorKey(fileobj=<socket.socket fd=360, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999)>, fd=360, events=1, data=1234)
[(SelectorKey(fileobj=<socket.socket fd=360, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999)>, fd=360, events=1, data=1234), 1)]
SelectorKey(fileobj=<socket.socket fd=360, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999)>, fd=360, events=1, data=1234) 1
<socket.socket fd=368, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 65364)> ('127.0.0.1', 65364)
"""