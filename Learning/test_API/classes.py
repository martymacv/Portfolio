import json
from datetime import date


class Car:
    def __init__(self, model, release, capacity, price, odometer, base=None):
        self.model = model
        self.release = release
        self.capacity = capacity
        self.price = price
        self.odometer = odometer
        self.base = base

    def description_car(self):
        print(f"Модель: {self.model}")
        print(f"Дата выпуска: {self.release}")
        print(f"Объем двигателя: {self.capacity}")
        print(f"Цена: {self.price}")
        print(f"Пробег: {self.odometer}")
        print(f"Количество колес: {self.base}")


class Truck(Car):
    def __init__(self, model, release, capacity, price, odometer):
        super().__init__(model, release, capacity, price, odometer)
        self.base = 8


audi = Car('audi', date(2012, 7, 11), 6.0, 2_000_000.00, 200_000, 4)
kamaz = Truck('kamaz', date(1987, 1, 1), 9.85, 10_000_000.0, 1000)
audi.description_car()
kamaz.description_car()

with open('json.json') as j:
    print(json.load(j))