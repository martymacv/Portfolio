import argparse
import asyncio
import socket
# import time
# from threading import Thread


class Controller:
    """Контроллер способен одновременно (в многопоточном режиме)
       опрашивать 10 устройств, которые производят различные измерения,
       преобразуя их в элетрический сигнал (мА или мВ)"""
    def __init__(self, ip="localhost", port=1024):
        self.ip = ip
        self.port = port
    """Что должен уметь наш контроллер:
       1. Отправлять get-запрос по UDP-сокету
       2. Сохранять значение в базу"""
    async def get(self):
        print(F"Controller IP: {self.ip}, port: {self.port} is run...")
        await asyncio.sleep(0.1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        sock.settimeout(10)
        while True:
            request = b"ping"
            sock.sendto(request, (self.ip, self.port))
            response = sock.recvfrom(1024)
            print(response)
            await asyncio.sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--sp", type=int, default=1024)
    parser.add_argument("--qp", type=int, default=1)

    args = parser.parse_args()

    start_port = args.sp
    quantity_ports = args.qp

    async def starter():
        await asyncio.gather(*[Controller(port=i).get() for i in range(start_port, start_port + quantity_ports)])

    asyncio.run(starter())


