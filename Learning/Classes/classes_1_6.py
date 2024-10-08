


class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

res = Loader.parse_format("4, 5, -6", Factory)

print(res)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(3, 5)
pt_copy = pt.clone()



TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    name = None

    def __new__(cls, *args, **kwargs):
        super().__new__(cls)
        cls.name = args[0]
        instance = [DialogLinux(), DialogWindows()][TYPE_OS]
        setattr(instance, 'name_class', cls.name)
        return instance


dlg1 = Dialog("Test")
TYPE_OS = 1
dlg2 = Dialog("Test")


class SingletonFive:
    __counter = 0
    __curr_instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__counter += 1
            cls.__curr_instance = super().__new__(cls)
        return cls.__curr_instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)

    def __int__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)

# Syngleton
# Чтобы создавать только один экземпляр класса

class DataBase:
    __instance = None
    # для реализации паттерна singleton не хватает применения магического метода
    # def __call__(cls, *args, **kwargs):
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))

db.connect()
db2.connect()


