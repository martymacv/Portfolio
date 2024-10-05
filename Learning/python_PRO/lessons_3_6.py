
import time
from math import factorial                   # функция из модуля math


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


def calculate_it(func, *args):
    start_time = time.perf_counter()
    func(*args)
    return time.perf_counter() - start_time


def get_the_fastest_func(funcs, arg=None):
    time_for_funcs = {calculate_it(func, arg): func for func in funcs}
    print(time_for_funcs, sep='\n')
    return time_for_funcs[min(time_for_funcs.keys())]


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))
