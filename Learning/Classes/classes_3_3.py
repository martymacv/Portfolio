import math
import sys


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @property
    def img(self):
        return self.__img

    @real.setter
    def real(self, real):
        self.__real = real

    @img.setter
    def img(self, img):
        self.__img = img

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return math.sqrt(self.real * self.real + self.img * self.img)


cmp = Complex("7", 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
sys.exit()
class ObjList:
    def __init__(self, data):
        self.__data = data  # ссылка на строку с данными;
        self.__prev = None  # ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
        self.__next = None  # ссылка на следующий объект связного списка (если объекта нет, то __next = None).

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @property
    def next(self):
        return self.__next

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @next.setter
    def next(self, obj):
        self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = None  # ссылка на первый объект связного списка (если список пуст, то head = None);
        self.tail = None  # ссылка на последний объект связного списка (если список пуст, то tail = None).
        self.count = 0

    def find_last_obj(self):
        i = 1
        last_obj = self.head
        while last_obj.next is not None:
            last_obj = last_obj.next
            i += 1
        return {
            'count': i,
            'last_obj': last_obj
        }

    def find_obj_by_index(self, indx):
        i = 0
        find_obj = self.head
        while i != indx:
            find_obj = find_obj.next
            i += 1
        return find_obj

    def __len__(self):
        if self.head is None:
            return 0
        return self.find_last_obj()['count']

    def __call__(self, indx, *args, **kwargs):
        if self.head is None or self.__len__() <= indx:
            pass
        if indx == 0:
            return self.head
        return self.find_obj_by_index(indx).data

    def add_obj(self, obj):
        """ добавление нового объекта obj класса ObjList в конец связного списка; """
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            last_obj = self.tail
            self.tail = obj
            last_obj.next = self.tail
            self.tail.prev = last_obj

    def remove_obj(self, indx):
        """ удаление объекта класса ObjList из связного
            списка по его порядковому номеру(индексу);
            индекс отсчитывается с нуля. """
        if self.head is None:
            return
        elif indx == 0 and self.head == self.tail:
            self.head = None
            self.tail = None
        elif indx == 0 and self.head is not None:
            self.head = self.head.next
            self.head.prev = None
        elif indx == self.__len__() - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            obj_to_remove = self.find_obj_by_index(indx)
            prev_obj = obj_to_remove.prev
            next_obj = obj_to_remove.next
            prev_obj.next = next_obj
            next_obj.prev = prev_obj


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
print(ln(2))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"

sys.exit()
linked_lst = LinkedList()
# print(linked_lst(0))
linked_lst.add_obj(ObjList("Sergey"))
print(f"{linked_lst(0).data = }")
# print(f"{linked_lst(1).data = }")
print()
linked_lst.add_obj(ObjList("Balakirev"))
print(f"{linked_lst(0).data = }")
print(f"{linked_lst(1).data = }")
print()
linked_lst.add_obj(ObjList("Python"))
print(f"{linked_lst(0).data = }")
print(f"{linked_lst(1).data = }")
print(f"{linked_lst(2).data = }")
print()
linked_lst.remove_obj(0)
print(f"{linked_lst(0).data = }")
print(f"{linked_lst(1).data = }")
# print(f"{linked_lst(2).data = }")
print()
linked_lst.add_obj(ObjList("Python ООП"))
print(f"{linked_lst(0).data = }")
print(f"{linked_lst(1).data = }")
print(f"{linked_lst(2).data = }")
print()
sys.exit()
class WordString:
    def __init__(self, string=None):
        self._string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    def __len__(self):
        return len(self.string.split())

    def __call__(self, *args, **kwargs):
        return self.string.split()[args[0]]


w1 = WordString()
w2 = WordString("Курс по Python ООП")
words = WordString()
words.string = "Курс  по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
sys.exit()
class Model:
    def __init__(self):
        self.db_row = dict()

    def query(self, **kwargs):
        self.db_row.update(kwargs)

    def __str__(self):
        if self.db_row:
            return f"Model: " + ", ".join(f"{key} = {value}" for key, value in self.db_row.items())
        else:
            return self.__class__.__name__


model = Model()
# model.query(id=1, fio='Sergey', old=33)
print(model)
sys.exit()
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))

book = Book(*lst_in)
print(book)
