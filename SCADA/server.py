import argparse
import asyncio
import socket


class Device:
    """Этот объект работает как эхо-сервер, ожидает запросов от контроллеров
       и отвечает на них, пересылая значение измеряемой величины (мА, мВ и пр.)"""
    def __init__(self, ip="", port=2000):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """Что должен уметь наш device:
       1. Обработать входящее сообщение (request)
       2. Адресно отправить ответное сообщение (respose)"""
    async def response(self):
        print(F"Device IP: {self.ip}, port: {self.port} is run...")
        await asyncio.sleep(0.1)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        while True:
            request, *address = self.sock.recvfrom(1024)
            self.sock.sendto(b"pong", *address)
            print(f"response {request} from {address}")
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

    # device = Device()

    async def starter():
        await asyncio.gather(*[Device(port=i).response() for i in range(2000, 2010)])
    #
    #
    asyncio.run(starter())
