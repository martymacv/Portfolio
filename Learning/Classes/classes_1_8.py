import sys

from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits


class EmailValidator:
    CHARS = ascii_lowercase + ascii_uppercase + digits + '_.'
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        if not len(args) and not len(kwargs):
            return None
        else:
            return cls.__instance

    @staticmethod
    def __is_email_str(email):
        a = len(email.split('@')) == 2
        print(email)
        print(a)
        if a:
            part1, part2 = email.split('@')
            print(part1, part2)
            b = (1 <= len(part1) <= 100) and part1.find('..') == -1
            print(b)
            c = (1 <= len(part2) <= 50) and part2.count('.') == 1
            print(c)
            return b and c
        return False

    @classmethod
    def get_random_email(cls):  # - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com
        eml = ''.join([choice(cls.CHARS) for _ in range(randint(1, 100))]) + '@' + ''.join([choice(cls.CHARS) for _ in range(randint(1, 50))])
        while not cls.check_email(eml):
            eml = ''.join([choice(cls.CHARS) for _ in range(randint(1, 100))]) + '@' + ''.join([choice(cls.CHARS) for _ in range(randint(1, 50))])
        return eml

    @classmethod
    def check_email(cls, email):  # - возвращает True, если email записан верно и False - в противном случае.
        return cls.__is_email_str(email)


em = EmailValidator()
print(em)
# res = EmailValidator.check_email("sc_lib@list.ru")  # True
#print(res)
res = EmailValidator.check_email("sc_lib@list_ru")  # False
print(res)

sys.exit(999)

class LinkedList:
    def __init__(self):
        self.head = None  # - ссылка на первый объект связного списка
        self.tail = None  # - ссылка на последний объект связного списка

    def add_obj(self, obj):  # - добавление нового объекта obj класса ObjList в конец связного списка;
        if self.head is None:
            self.head = obj
        elif self.tail is None:
            self.tail = obj
            self.head.set_next(self.tail)
            self.tail.set_prev(self.head)
        else:
            curr = self.tail
            self.tail = obj
            curr.set_next(self.tail)
            self.tail.set_prev(curr)

    def remove_obj(self):  # - удаление последнего объекта из связного списка;
        if self.tail is None:
            self.head = None
        elif self.head is None:
            pass
        else:
            self.tail.get_prev().set_next(None)
            self.tail = None

    def get_data(self):  # - получение списка из строк локального свойства __data всех объектов связного списка.
        obj = self.head
        obj_list = []
        while obj is not None:
            obj_list.append(obj.get_data())
            obj = obj.get_next()
        print(obj_list)


class ObjList:
    def __init__(self, data=None):
        self.__next = None  # - ссылка на следующий объект связного списка
        self.__prev = None  # - ссылка на предыдущий объект связного списка
        self.__data = data  # - строка с данными.

    def set_next(self, obj):  # - изменение приватного свойства __next на значение obj;
        self.__next = obj

    def set_prev(self, obj):  # - изменение приватного свойства __prev на значение obj;
        self.__prev = obj

    def get_next(self):  # - получение значения приватного свойства __next;
        return self.__next

    def get_prev(self):  # - получение значения приватного свойства __prev;
        return self.__prev

    def set_data(self, data):  # - изменение приватного свойства __data на значение data;
        self.__data = data

    def get_data(self):  # - получение значения приватного свойства __data.
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))
lst.add_obj(ObjList("данные 5"))
res = lst.get_data()


sys.exit(999)

# Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес. Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).


# Для реализации этой схемы программе предлагается объявить три класса:
class IpGen:
    __ip_list = set()

    @classmethod
    def generate_random_ip(cls):
        new_ip_addr = ".".join([str(random.randint(0, 255)) for _ in range(4)])
        if new_ip_addr in cls.__ip_list:
            cls.generate_random_ip()
        else:
            return new_ip_addr


class Data:  # - для описания пакета информации.
    def __init__(self, data: str, ip: str):
        # передаваемые        данные(строка);
        self.data = data
        # IP - адрес        назначения.
        self.ip = ip


class Server:  # - для описания работы серверов в сети;
    def __init__(self):
        # список        принятых        пакетов(объекты        класса        Data, изначально        пустой);
        self.buffer = []
        # IP - адрес        текущего        сервера.
        self.ip = IpGen.generate_random_ip()
        self.links = []

    def send_data(self, data: Data):
        # для    отправки    информационного    пакета    data(объекта    класса    Data) с    указанным
        # IP - адресом    получателя(пакет    отправляется    роутеру    и    сохраняется    в    его
        # буфере - локальном    свойстве    buffer);
        for router in self.links:
            router.buffer.append(data)

    def get_data(self):
        # возвращает    список    принятых    пакетов(если    ничего    принято    не    было, то    возвращается
        # пустой    список) и    очищает    входной    буфер;
        l = self.buffer
        self.buffer = []
        return l

    def get_ip(self):
        # возвращает    свой    IP - адрес.
        return self.ip


class Router:  # - для описания работы роутеров в сети (в данной задаче полагается один роутер);
    def __init__(self):
        # список    для    хранения    принятых    от    серверов    пакетов(объектов    класса    Data).
        self.buffer = []
        self.links = dict()

    def link(self, server: Server):
        # для    присоединения    сервера    server(объекта    класса    Server) к    роутеру(для    простоты, каждый
        # сервер    соединен    только    с    одним    роутером);
        self.links[server.ip] = server
        server.links.append(self)

    def unlink(self, server: Server):
        # для    отсоединения    сервера    server(объекта    класса    Server) от    роутера;
        del self.links[server.ip]

    def send_data(self):
        # для    отправки    всех    пакетов(объектов    класса    Data) из    буфера    роутера
        # соответствующим    серверам(после    отправки    буфер    должен    очищаться).
        for msg in self.buffer:
            self.links[msg.ip].buffer.append(msg.data)
        self.buffer = []



# Серверы будут создаваться командой:
# При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.

# Далее, роутер должен создаваться аналогичной командой:

# А, пакеты данных, командой:

server1 = Server()
router = Router()
server2 = Server()
server1.send_data(Data("Hello, server2", server2.get_ip()))
server2.send_data(Data("Hello, server2", server2.get_ip()))
server1.send_data(Data("Hello, server2", server2.get_ip()))
router.link(server1)
router.link(server2)
router.unlink(server2)
router.link(server2)
router.send_data()
server2.send_data(Data(server2.buffer[0], server1.get_ip()))
print(server2.get_data())


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
