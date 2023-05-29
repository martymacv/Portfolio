import socket
from threading import Thread


udp_clients = [[socket.socket(socket.AF_INET, socket.SOCK_DGRAM), i] for i in range(2222, 2223)]


def func1(udp_client_):
    udp_client_[0].settimeout(100)
    udp_client_[0].sendto(b"Hello! i'm 1111", ("127.0.0.1", udp_client_[1]))
    request, address = udp_client_[0].recvfrom(1024)
    # udp_client.sendto(b"pong", address)
    print(request, *address)


for udp_client in udp_clients:
    Thread(target=func1(udp_client)).start()
# Thread(target=func2(udp_client.recvfrom(1024))).start()

# request, address = udp_client.recvfrom(1024)
# udp_client.sendto(b"ping", address)

