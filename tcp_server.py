import socket

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 绑定地址
sockfd.bind(('0.0.0.0',9999))

# 设置监听
sockfd.listen(128)

while True:
    # 等待处理客户端连接
    print('Waiting for connect ...')
    connfd, addr = sockfd.accept()
    print('Connect from: ',addr)    # 打印客户端地

    fw = open('b.py','wb') 

    # 消息收发
    while True:
        data = connfd.recv(4096)          
        if not data:
            break
        fw.write(data)       
        # print('Receive Msg: ', data.decode())
        # n = connfd.send(b'I see.')       # 英文加b, 变量中文需要.encode()
        # print('Send %d bytes' %n)
   
fw.close()
    #关闭套接字
connfd.close()
sockfd.close()