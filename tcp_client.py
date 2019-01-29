from socket import * 

# 创建套接字
sockfd = socket()

# 发起连接请求
server_addr = ('127.0.0.1',8800)    # 172.40.76.178
sockfd.connect(server_addr)


# 消息收发
fr =  open('a.png', 'rb')
while True:
    r = fr.read(4096) 
    sockfd.send(r)
    if not r:
        break  
# while True:
#     data = sockfd.recv(1024)
    # print('From server: ', data.decode())
fr.close()
sockfd.close()