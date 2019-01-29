# simple_svr.py
# 简单网络服务器
import socket
address = ("0.0.0.0", 9999)
## 创建socket: socket
server = socket.socket()
## 绑定地址:bind()函数
server.bind(address)
## 监听: listen()函数
server.listen(10) 
print("服务器已启动:", address)
## 接受请求:accept()函数
sockfd, addr = server.accept()
print("收到客户端请求:", addr)
## 数据接收:recv()
data = sockfd.recv(1024)
print(data.decode())
## 关闭连接
sockfd.close() #关闭通信socket
server.close() #关闭监听socket