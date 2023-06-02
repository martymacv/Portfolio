import argparse
import asyncio
import socket
import time
# from threading import Thread


class Controller:
    """Контроллер способен одновременно (в многопоточном режиме)
       опрашивать 10 устройств, которые производят различные измерения,
       преобразуя их в элетрический сигнал (мА или мВ)"""
    def __init__(self, ip="localhost", port=2000):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """Что должен уметь наш контроллер:
       1. Отправлять get-запрос по UDP-сокету
       2. Сохранять значение в базу"""
    async def get(self):
        print(F"Controller IP: {self.ip}, port: {self.port} is run...")
        await asyncio.sleep(0.1)
        self.sock.settimeout(55)
        while True:
            request = b"ping"
            self.sock.sendto(request, (self.ip, self.port))
            # await asyncio.sleep(0.1)
            print(f"request {request}")
            response, *address = self.sock.recvfrom(1024)
            print(f"response {response} from {address}")
            await asyncio.sleep(5)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Script so useful.')
    # parser.add_argument("--sp", type=int, default=2000)
    # parser.add_argument("--qp", type=int, default=1)
    #
    # args = parser.parse_args()
    #
    # start_port = args.sp
    # quantity_ports = args.qp

    async def starter():
        await asyncio.gather(*[Controller(port=i).get() for i in range(2000, 2010)])

    asyncio.run(starter())


