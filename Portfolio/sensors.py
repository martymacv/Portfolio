import asyncio
import random
import socket
import json
from threading import Thread

import cx_Oracle

from registers import Register

"""Итак, я хочу создавать объекты типа "Датчик", который может:
    1. обмениваться данными с агентом (клентом или другим сервером)
    2. генерировать данные
    3. сериализовать данные
    4. запускать из командной строки с параметрами
    5. валидировать входящие запросы
    6. логировать ошибки"""


class Sensor:
    def __init__(self, type_server, sensor_id, ip, port, registers):
        self.__type_server = type_server
        self.__sensor_id = sensor_id
        self.__ip = ip
        self.__port = port
        self.registers = registers
        self.__len_registers = len(self.registers)
        if self.__type_server == "UDP_SERVER":
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif self.__type_server == "TCP_SERVER":
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            pass
        self.__save_config(self.__type_server, self.__sensor_id, self.__ip, self.__port)

    @classmethod
    def __save_config(cls, type_server, sensor_id, ip, port):
        with open(f"sensors_log/sensor_{sensor_id[-4:]}_config.json", "w") as f:
            json.dump({"type_server": type_server, "sensor_id": sensor_id, "ip": ip, "port": port}, f, indent=4)

    # @classmethod
    # def __save_signals(cls, sensor_id, signals):
    #     with open(f"sensors_log/sensor_{sensor_id[-4:]}_config.json", "r+") as f:
    #         # f.write("\n\n")
    #         json.dump({"register_id": signals}, f, indent=4)

    def run(self):

        # self.__save_signals(self.__sensor_id, self.registers)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.__ip, self.__port))
        print(f"{self.__sensor_id} is run...")
        i = 0
        output = [b'' for _ in range(self.__len_registers)]
        while True:
            request, address = self.sock.recvfrom(1024)
            for reg in self.registers:
                output[reg.unit_id - 1] = reg.value[i % reg.value[~0]]
            self.sock.sendto(b''.join(output), address)
            print(request, *address)
            i += 1
            # return request, *address

    async def start(self):
        await asyncio.gather(*self.__registers)


async def start(regs):
    await asyncio.gather(*[regs[i].run() for i in range(10000)])


if __name__ == "__main__":
    sens_id = "TEMPERATURE_SENSOR_" + str(777).rjust(4, "0")
    sensor_1 = Sensor("UDP_SERVER", sens_id, "", 2222, [Register(1, (-25000, 25000), "R", 1),
                                                        Register(10, (-2500, 2500), "R", 2),
                                                        Register(100, (0, 25000), "R", 3)])
    sensor_1.run()
    # i = 0
    # output = [0, 0, 0]
    # while True:
    #     for register in sensor_1.registers:
    #         output[register.unit_id - 1] = register.value[i % register.value[~0]]
    #     print(output)
    #     i += 1
    # создаем объект Sensor передаем в него объекты Register и запускаем последние асинхронно
    # asyncio.run(start(registers))
    # for i in registers:
    #     asyncio.run(i.run())
    # for register in registers:
    #     Thread(target=register.run).start()

    # sens_id = "TEMPERATURE_SENSOR_" + str(777).rjust(4, "0")
    # sensor = Sensor("UDP_SERVER", sens_id, "localhost", 2222)
    # abc = sensor.getvalue[0]
    # sens_id = "TEMPERATURE_SENSOR_" + str(999).rjust(4, "0")
    # sensor_2 = Sensor("UDP_SERVER", sens_id, "localhost", 1111)
    # Thread(target=sensor_1.run).start()
    # Thread(target=sensor_2.run).start()

    with cx_Oracle.connect(user=user,
                           password=password,
                           tns=tns,
                           encoding='utf-8') as db_conn:
        with db_conn.cursor() as cursor:
            sql_text = (f"delete from {etl_objects[i][0]}.{etl_objects[i][1]} "
                        "where my_column = 'my_variable'")
            cursor.execute(sql_text)
            cursor.execute('commit')
            sql_text = (f"insert into {etl_objects[i][0]}.{etl_objects[i][1]} "
                        "select * "
                        f"from {etl_objects[i][0]}.{etl_objects[i][1]}@src_dblink "
                        "where my_column = 'my_variable';")
            cursor.execute(sql_text)
            cursor.execute('commit')