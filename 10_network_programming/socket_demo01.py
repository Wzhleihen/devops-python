import socket
import sys

# 创建套接字 默认情况下是流协议
server = socket.socket()

# 绑定IP和端口
addr = '127.0.0.1', 9999
server.bind(addr)

# 监听
server.listen() # 表示最大连接数

print(server,file=sys.stderr)  # 打印套接字对象
# <socket.socket fd=368, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999)>
# fd: 文件描述符, family: 协议族, type: 套接字类型, proto: 协议, laddr: 本地地址 

network, addr = server.accept() # 阻塞方法
print(type(network), network)
print(network.getpeername()) # 获取客户端地址
print(network.getsockname()) # 获取服务端地址


network.send(b'hello') # 发送数据


# 接收数据
data = network.recv(1024) # 接收数据
print(type(data), data) # <class 'bytes'> b'hello'


# 再次回送消息
msg = f"data={data}"
network.send(msg.encode())


# 再开启一个客户端连接
s1, raddr1 = server.accept()   # 注意，accept 方法会从 listen() 队列中取出一个连接，默认情况下， listen只有一个
data = s1.recv(1024)
print(data, '~~~~~~~~~~~~~')


# 关闭
server.close()