import sys

# считывание строки и разбиение ее по пробелам
lst_in = '8 11 abcd -7.5 2.0 -5'.split()


def int_filter(num: any) -> int:
    try:
        return int(num)
    except ValueError:
        pass


print(sum(map(int, filter(int_filter, lst_in))))



sys.exit(999)
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)

try:
    print(pt.z)
except AttributeError:
    print("Атрибут с именем z не существует")
