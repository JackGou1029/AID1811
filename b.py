# 客户端
from socket import *
from threading import Thread


ADR = ('172.40.76.108', 5687)
udptocket = None

flag = True


# 收信息
def recv():
    global flag
    while flag:
        data, adr = udptocket.recvfrom(4096)
        if not data:
            flag = False
            continue
        print("\r" + data.decode() + "\n>> ", end='')


# 发信息
def sendto():
    # 初始化用户
    udptocket.sendto("%$".encode(), ADR)
    
    while flag:
        msg = input("\r>> ").encode()
        udptocket.sendto(msg, ADR)


# 主函数
def main():
    global udptocket
    udptocket = socket(AF_INET, SOCK_DGRAM)
    udptocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    tr = Thread(target=recv)
    ts = Thread(target=sendto)

    tr.start()
    ts.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()