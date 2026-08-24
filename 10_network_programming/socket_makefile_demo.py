import socket

server = socket.socket()
server.bind(('localhost', 8081))
server.listen()

network, addr = server.accept()
print('-' * 30)
f = network.makefile('rw')

x = f.read(5)  # 阻塞方法，读取5个字节
print('~' * 30)

msg = "from {}:{} data={}".format(*addr, x)

f.write(msg)  # 阻塞方法，写入数据

network.close() # 关闭socket
f.close()  # 关闭文件
server.close()