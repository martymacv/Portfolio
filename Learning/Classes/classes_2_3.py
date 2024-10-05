import sys


class TVProgram:
    def __init__(self, chanel_name):
        self.chanel_name = chanel_name
        self.items = []  # - список из телепередач (изначально список пуст)

    def add_telecast(self, tl):  # - добавление новой телепередачи в список items;
        self.items.append(tl)

    def remove_telecast(self, indx):  # - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
        del self.items[indx]


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id  # - порядковый номер (целое число);
        self.__name = name  # - наименование телепередачи (строка);
        self.__duration = duration  # - длительность телепередачи в секундах (целое число).

    def get_uid(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_duration(self):
        return self.__duration

    def set_uid(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_duration(self, duration):
        self.__duration = duration

    uid = property(get_uid, set_uid)  # - для записи и считывания из локального атрибута __id;
    name = property(get_name, set_name)  # - для записи и считывания из локального атрибута __name;
    duration = property(get_duration, set_duration)  # - для записи и считывания из локального атрибута __duration.


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")

sys.exit(999)


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight  # - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число)
        self.__things = []  # - список вещей в рюкзаке (изначально список пуст)

    def get_things(self) -> list:
        return self.__things

    things = property(get_things)

    def add_thing(self, thing):
        """ добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight)
            не будет превышен, иначе добавление не происходит); """
        if self.get_total_weight() < self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):  # - удаление предмета по индексу списка __things;
        del self.__things[indx]

    def get_total_weight(self):  # - возвращает суммарный вес предметов в рюкзаке.
        print(sum(map(lambda x: x.weight, self.__things)))
        return sum(map(lambda x: x.weight, self.__things))


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
print(w)
