import sys
import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def __setattr__(self, key, value):
        try:
            if self.__dict__[key] is None:
                if key == 'slot_1' and type(value).__name__ == 'Mechanical':
                    object.__setattr__(self, key, value)
                elif key == 'slot_2' and type(value).__name__ == 'Aragon':
                    object.__setattr__(self, key, value)
                elif key == 'slot_3' and type(value).__name__ == 'Calcium':
                    object.__setattr__(self, key, value)
            else:
                if value is None:
                    object.__setattr__(self, key, value)
        except KeyError:
            object.__setattr__(self, key, None)

    def add_filter(self, slot_num, filter):
        if slot_num == 1:
            self.slot_1 = filter
        elif slot_num == 2:
            self.slot_2 = filter
        elif slot_num == 3:
            self.slot_3 = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        return all(map(lambda x: x is not None, [self.slot_1, self.slot_2, self.slot_3])) and all(map(lambda x: 0 <= time.time() - x.date <= self.MAX_DATE_FILTER, [self.slot_1, self.slot_2, self.slot_3]))


class Filter:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        try:
            self.__dict__[key]
        except KeyError:
            object.__setattr__(self, key, value)


class Aragon(Filter):
    def __init__(self, date: float):
        super().__init__(date)


class Mechanical(Filter):
    def __init__(self, date: float):
        super().__init__(date)


class Calcium(Filter):
    def __init__(self, date: float):
        super().__init__(date)


a = Mechanical(time.time())
print(f"{a.date = }")
a.date = time.time()
print(f"{a.date = }")

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
my_water.remove_filter(1)
w = my_water.water_on() # True
print(w)

sys.exit()
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def set_a(self, number):
        self.__a = number

    a = property(get_a, set_a)

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, number):
        self.__b = number

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, number):
        self.__c = number

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION', ):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            if type(value) in (float, int) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
                object.__setattr__(self, key, value)


d = Dimensions(10, 20, 30)

a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
print(d.a, d.b, d.c)


sys.exit()
class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        print(key, value)
        if key in ('_Circle__x', '_Circle__y', 'x', 'y') and type(value) in (int, float):
            object.__setattr__(self, key, value)
        elif key in ('_Circle__radius', 'radius') and type(value) in (int, float):
            if value >= 0.0:
                object.__setattr__(self, key, value)
            else:
                pass
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_radius(self):
        return self.__radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, radius):
        self.__radius = radius

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    radius = property(get_radius, set_radius)


circle = Circle(10.5, 7, 22)
circle = Circle('', 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует

sys.exit()

class SmartPhone:
    def __init__(self, model):
        self.model = model  # - марка смартфона (строка);
        self.apps = []  # - список из установленных приложений (изначально пустой).

    def add_app(self, app):  # - добавление нового приложения на смартфон (в конец списка apps);
        if type(app) not in list(map(type, self.apps)):
            self.apps.append(app)

    def remove_app(self, app):  # - удаление приложения по ссылке на объект app.
        self.apps.remove(app)


class AppVK:  # - класс приложения ВКонтаке;
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:  # - класс приложения YouTube;
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:  # - класс приложения телефона.
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)

sys.exit(999)

class Museum:
    def __init__(self, name):
        self.name = name  # - название музея (строка);
        self.exhibits = []  # - список экспонатов (изначально пустой список).

    def add_exhibit(self, obj):  # - добавление нового экспоната в музей (в конец списка exhibits);
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):  # - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):  # - получение информации об экспонате (строка) по индексу списка
        name, descr = self.exhibits[indx].name, self.exhibits[indx].descr
        return f"Описание экспоната {name}: {descr}"


class Picture:  # - для картин;
    def __init__(self, name, author, descr):
        self.name = name  # - название;
        self.author = author  # - художник;
        self.descr = descr  # - описание


class Mummies:  # - для мумий;
    def __init__(self, name, location, descr):
        self.name = name  # - имя мумии;
        self.location = location  # - место находки;
        self.descr = descr  # - описание


class Papyri:  # - для папирусов.
    def __init__(self, name, date, descr):
        self.name = name  # - название папируса;
        self.date = date  # - датировка (строка);
        self.descr = descr  # - описание


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
                        "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)


sys.exit(999)
class Course:
    def __init__(self, name):
        self.name = name  # - название курса (строка);
        self.modules = []  # - список модулей в курсе (изначально список пуст).

    def add_module(self, lesson):  # - добавление нового модуля в конце списка modules;
        self.modules.append(lesson)

    def remove_module(self, indx):  # - удаление модуля из списка modules по индексу в этом списке.
        del self.modules[indx]


class Module:
    def __init__(self, name):
        self.name = name  # - название модуля;
        self.lessons = []  # - список из уроков (объектов класса LessonItem)

    def add_lesson(self, lesson):  # - добавление в модуль (в конец списка lessons);
        self.lessons.append(lesson)

    def remove_lesson(self, indx):  # - удаление урока по индексу в списке lessons.
        del self.lessons[indx]


class LessonItem:
    attrs = {
        'title': (str, ),
        'practices': (int, ),
        'duration': (int, )
    }

    def __init__(self, title, practices, duration):
        self.title = title  # - название урока (строка);
        self.practices = practices  # - число практических занятий (целое положительное число);
        self.duration = duration  # - общая длительность урока (целое положительное число).

    def __setattr__(self, key, value):
        if type(value) in self.attrs[key]:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        else:
            object.__delattr__(self, item)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)


sys.exit(999)

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []  # - список товаров (изначально список пустой).

    def add_product(self, product):  # - добавление нового товара в магазин (в конец списка goods);
        self.goods.append(product)

    def remove_product(self, product):  # - удаление товара product из магазина (из списка goods);
        self.goods.remove(product)


class Product:
    last_id = 0
    attrs = {
        'id': (int, ),
        'name': (str, ),
        'weight': (int, float),
        'price': (int, float)
    }

    def __init__(self, name, weight, price):
        self.id = self.get_next_id()  # - уникальный идентификационный номер товара
        self.name = name  # - название товара (строка);
        self.weight = weight  # - вес товара (целое или вещественное положительное число);
        self.price = price  # - цена (целое или вещественное положительное число).

    def __setattr__(self, key, value):
        if type(value) in self.attrs[key] and self.is_greater(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)

    @classmethod
    def get_next_id(cls):
        cls.last_id += 1
        return cls.last_id

    @staticmethod
    def is_greater(value):
        if type(value) in (int, float):
            return value > 0
        return True


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
# shop.remove_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id}, {p.name}, {p.weight}, {p.price}")

sys.exit(999)


class Book:
    attrs = {
        'title': str, 'author': str, 'pages': int, 'year': int
    }

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title  # - заголовок книги (строка, по умолчанию пустая строка);
        self.author = author  # - автор книги (строка, по умолчанию пустая строка);
        self.pages = pages  # - число страниц (целое число, по умолчанию 0);
        self.year = year  # - год издания (целое число, по умолчанию 0).

    def __setattr__(self, key, value):
        if type(value) == self.attrs[key]:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
print(book.title)
print(book.author)
print(book.pages)
print(book.year)

print('W' * 777)
