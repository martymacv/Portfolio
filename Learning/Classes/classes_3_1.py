import sys


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
