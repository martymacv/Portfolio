import sys
from math import sqrt


class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def check_value(self, value):
        return type(value) == str and self.min_length <= len(value) <= self.max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(value)
        if self.check_value(value):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_length=10000):
        self.max_length = max_length

    def check_value(self, value):
        return type(value) in (int, float) and 0 <= value <= self.max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(value)
        if self.check_value(value):
            setattr(instance, self.name, value)


class SuperShop:
    name = StringValue(min_length=2, max_length=50)
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        cls.__instance._name = None
        return cls.__instance

    def __init__(self, name: str):
        self.name = name  # - название магазина (строка);
        self.goods = list()  # - список из товаров.

    def add_product(self, product):  # - добавление товара в магазин (в конец списка goods);
        self.goods.append(product)

    def remove_product(self, product):  # - удаление товара из магазина (из списка goods).
        del self.goods[self.goods.index(product)]


class Product:
    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
    # max_value - максимально допустимое значение
    name = StringValue(min_length=2, max_length=50)
    price = PriceValue(max_length=10000)
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        cls.__instance._name = None
        cls.__instance._price = None
        return cls.__instance

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

sys.exit(999)
class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length  # - минимальное число символов в строке;
        self.max_length = max_length  # - максимальное число символов в строке.

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    __instance = None
    login = StringValue(validator=ValidateString())  # - для ввода логина;
    password = StringValue(validator=ValidateString())  # - для ввода пароля;
    email = StringValue(validator=ValidateString())  # - для ввода Email.

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        cls.__instance._login = None
        cls.__instance._password = None
        cls.__instance._email = None
        return cls.__instance

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):  # - возвращает список из значений полей в порядке [login, password, email];
        return [self._login, self._password, self._email]

    def show(self):  # - выводит в консоль многострочную строку в формате:
        print("<form>")
        print(f"Логин: <{self._login}>")
        print(f"Пароль: <{self._password}>")
        print(f"Email: <{self._email}>")
        print("</form>")


min_len = 3
max_len = 100
validate = ValidateString(min_length=3, max_length=100)
st = StringValue(validator=ValidateString(min_len, max_len))
form = RegisterForm("логин", "пароль", "email")
# print(form.login)
# form.login = "login"
# print(form.login)
form.show()

sys.exit(999)


class FloatValue:
    @classmethod
    def check_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self._value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for _ in range(self.M)] for _ in range(self.N)]


table = TableSheet(5, 3)
count = 1
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = count
        count += 1


else:
    print("Hello")

sys.exit(999)


class PhoneBook:
    phone_list = list()

    @classmethod
    def add_phone(cls, phone):  # - добавление нового номера телефона (в список);
        cls.phone_list.append(phone)

    @classmethod
    def remove_phone(cls, indx):  # - удаление номера телефона по индексу списка;
        del cls.phone_list[indx]

    @classmethod
    def get_phone_list(cls):  # - получение списка из объектов всех телефонных номеров.
        return cls.phone_list


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number  # - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
        self.fio = fio  # - Ф.И.О. владельца номера (строка).


sys.exit(999)


class PathLines:
    x0 = 0
    y0 = 0

    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):  # - возвращает список из объектов класса LineTo(если объектов нет, то пустой список);
        return self.lines

    def get_length(self):  # - возвращает суммарную длину пути(сумма длин всех линейных сегментов);
        x0 = 0
        y0 = 0
        length = 0
        for line in self.lines:
            x1, y1 = line.x, line.y
            length += sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            x0, y0 = x1, y1
        return length

    def add_line(self, line):  # - добавление нового линейного сегмента(объекта класса LineTo) в конец маршрута.
        self.lines.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)

sys.exit(999)


def print_group(fl, summ, byte_format):
    [print(f) for f in fl]
    print("----------")
    print(f"Summary: {summ} {byte_format}")
    print()


with open('files.txt', 'r', encoding='utf=8') as file_in:
    file_list = [tuple(line.split()) for line in file_in.readlines()]

file_group = dict()
for file in file_list:
    file_group[file[0].split('.')[1]] = file_group.get(file[0].split('.')[1],
                                                       {'file_list': list(), 'bytes_format': dict()})
    file_group[file[0].split('.')[1]]['file_list'].append(file[0])
    file_group[file[0].split('.')[1]]['bytes_format'][file[2]] = file_group[file[0].split('.')[1]]['bytes_format'].get(
        file[2], list())
    file_group[file[0].split('.')[1]]['bytes_format'][file[2]].append(int(file[1]))
for group in sorted(file_group):
    file_group[group]['file_list'] = sorted(file_group[group]['file_list'])
    table_byte_types = ['B', 'KB', 'MB', 'GB']
    byte_types = sorted(file_group[group]['bytes_format'].keys(), reverse=True, key=lambda x: table_byte_types.index(x))
    summa = [0, '']
    for i in range(len(byte_types)):
        summa[0] += sum(list(map(lambda x: x * (1024 ** (table_byte_types.index(byte_types[i]) + 1)),
                                 file_group[group]['bytes_format'][byte_types[i]])))
        summa[1] = byte_types[0]
    count = 1
    while (summa[0] // (1024 ** count)) > 1023:
        count += 1
    summa[0] = int(summa[0] / (1024 ** count) + 0.5)
    summa[1] = table_byte_types[count - 1]
    print_group(file_group[group]['file_list'], summa[0], summa[1])
sys.exit(999)

name_count = dict()

for _ in range(int(input())):
    exist_name = input().split('@')[0]
    while exist_name[~0].isdigit():
        exist_name = exist_name[:~0]
    name_count[exist_name] = name_count.get(exist_name, 0) + 1

for _ in range(int(input())):
    notexist_name = input()
    if name_count.get(notexist_name, 0):
        notexist_name += str(name_count[notexist_name] - 1)
    notexist_name += '@beegeek.bzz'
    print(notexist_name)
