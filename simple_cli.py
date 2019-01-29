# simple_cli.py
# 简单客户端
import socket
address = ("127.0.0.1", 9999)
## 创建socket
client = socket.socket()
## 连接服务器:connect函数
client.connect(address)
## 发送数据:send()函数
msg = "This is test string."
client.send(msg.encode())
print("消息已发送")
## 关闭连接
client.close()