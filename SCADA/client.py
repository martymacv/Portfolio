import argparse
import asyncio
import socket
import time
from py_class_learn import Modbus
from PModbus import modbus_client
from threading import Thread, Lock, Semaphore


class Controller:
    """Контроллер способен последовательно опрашивать любое количество
       подключенных к сети устройств, которые производят различные измерения,
       преобразуя их в элетрический сигнал (мА или мВ)"""
    ip = "localhost"
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client = modbus_client.MBAPClient()

    def __init__(self, port=2000):
        self.port = port
    """Что должен уметь наш контроллер:
       1. Отправлять get-запрос по UDP-сокету
       2. Сохранять значение в базу"""

    def get(self):
        Controller.udp_socket.settimeout(5)
        try:
            request = Controller.client.get_register_values(0, 1)
            Controller.udp_socket.sendto(request, (Controller.ip, self.port))
            print(f"request {request}")
            response, *address = Controller.udp_socket.recvfrom(1024)
            print(f"response {response} from {address}")
        except ConnectionResetError:
            print("ConnectionResetError")
        except TimeoutError:
            self.get()


if __name__ == "__main__":

    connections = [Controller(port=i) for i in range(2000, 2010)]

    while True:
        for connection in connections:
            connection.get()

