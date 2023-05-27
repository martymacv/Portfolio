import random
import socket
import json
from threading import Thread

"""Итак, я хочу создавать объекты типа "Датчик", который может:
    1. обмениваться данными с агентом (клентом или другим сервером)
    2. генерировать данные
    3. сериализовать данные
    4. запускать из командной строки с параметрами
    5. валидировать входящие запросы
    6. логировать ошибки"""


class Sensor:
    def __init__(self, type_server, sensor_id, ip, port):
        self.__type_server = type_server
        self.__sensor_id = sensor_id
        self.__ip = ip
        self.__port = port
        if self.__type_server == "UDP_SERVER":
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif self.__type_server == "TCP_SERVER":
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            pass

    @classmethod
    def __save_config(cls, type_server, sensor_id, ip, port):
        with open(f"sensors_log/sensor_{sensor_id[-4:]}_config.json", "w") as f:
            json.dump({"type_server": type_server, "sensor_id": sensor_id, "ip": ip, "port": port}, f, indent=4)

    def run(self):
        self.__save_config(self.__type_server, self.__sensor_id, self.__ip, self.__port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.__ip, self.__port))
        print(f"{self.__sensor_id} is run...")
        while True:
            request, address = self.sock.recvfrom(1024)
            self.sock.sendto(b"ping", address)
            print(request, *address)
            # return request, *address


if __name__ == "__main__":
    sens_id = "TEMPERATURE_SENSOR_" + str(777).rjust(4, "0")
    sensor_1 = Sensor("UDP_SERVER", sens_id, "localhost", 2222)
    sens_id = "TEMPERATURE_SENSOR_" + str(999).rjust(4, "0")
    sensor_2 = Sensor("UDP_SERVER", sens_id, "localhost", 1111)
    Thread(target=sensor_1.run).start()
    Thread(target=sensor_2.run).start()

