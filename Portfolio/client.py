import socket
from threading import Thread

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.sendto(b"Hello! i'm 1111", ("127.0.0.1", 1111))
udp_client.sendto(b"Hello! i'm 2222", ("127.0.0.1", 2222))


def func1(recvfrom):
    request, address = recvfrom
    udp_client.sendto(b"pong", address)
    print(request, *address)


def func2(recvfrom):
    request, address = recvfrom
    udp_client.sendto(b"pong", address)
    print(request, *address)


Thread(target=func1(udp_client.recvfrom(1024))).start()
Thread(target=func2(udp_client.recvfrom(1024))).start()

# request, address = udp_client.recvfrom(1024)
# udp_client.sendto(b"ping", address)

