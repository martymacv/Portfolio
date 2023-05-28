import asyncio
import random
import socket
import struct
import json
from threading import Thread


class Register:
    """Объекты этого класса должны хранить в себе данные массив данных, по которому можно воспроизвести сигнал"""
    def __init__(self, quantity_point, chart_limits, function_code, unit_id):
        self.__quantity_point = quantity_point
        self.__minvalue, self.__maxvalue = chart_limits
        # self.__function_code = function_code
        self.unit_id = unit_id
        # self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.value = self.__signal_gen()

    """Этот метод будет принадлежать другому классу - сигнал"""
    def __signal_gen(self):
        return tuple([struct.pack(">H" if self.__minvalue + self.__maxvalue >= self.__maxvalue else ">h",
                                  random.randint(self.__minvalue, self.__maxvalue))
                      for _ in range(self.__quantity_point)] + [self.__quantity_point])

    # async def run(self):
    #     # self.__save_config(self.__type_server, self.__sensor_id, self.__ip, self.__port)
    #     values = self.__signal_gen()
    #     self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     self.__sock.bind(("localhost", self.__unit_id))
    #     print(f"{self.__unit_id} is run...", end='\n')
    #     i = 0
    #     while True:
    #         if i == self.__quantity_point:
    #             i = 0
    #         await asyncio.sleep(0.005)
    #         request, address = self.__sock.recvfrom(1024)
    #         await asyncio.sleep(0.005)
    #         message = struct.pack(">h", values[i % 100])
    #         self.__sock.sendto(message, address)
    #         print(request, *address)
    #         i += 1


if __name__ == '__main__':
    register = Register(10, (-10, 10), "R", 1)
    print(register.value)
