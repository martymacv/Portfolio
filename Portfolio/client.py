import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.sendto(b"Hello!", ("127.0.0.1", 2222))

request, address = udp_client.recvfrom(1024)
udp_client.sendto(b"ping", address)
print(request, *address)