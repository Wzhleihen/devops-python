import socketserver


# 创建一个基础的请求处理类
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("=" * 30)
        print(repr(self.request))  # self.request是一个socket对象
        print(self.client_address)  # 客户端地址
        
server = socketserver.TCPServer(('localhost', 9999), MyTCPHandler)
print(server)
server.handle_request()  # 处理一个请求 