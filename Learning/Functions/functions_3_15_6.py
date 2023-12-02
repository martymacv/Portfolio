# Встроенные функции map, filter, reduce
#
# Встроенная функция map() имеет сигнатуру map(func, *iterables)
def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)  # используем встроенную функцию map()

print(new_numbers)

for num in new_numbers:  # итерируем циклом for
    print(num)


def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]

# Чтобы получить из итератора список, нужно воспользоваться функцией list()
new_numbers = list(map(func, numbers1, numbers2, numbers3))  # преобразуем итератор в список

print(new_numbers)

circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]

result1 = list(map(round, circle_areas, [1] * 6))  # округляем числа до 1 знака после запятой
result2 = list(map(round, circle_areas, range(1, 7)))  # округляем числа до 1,2,...,6 знаков после запятой

print(circle_areas)
print(result1)
print(result2)


# Встроенная функция filter() имеет сигнатуру filter(func, iterable)


def func(elem):
    return elem >= 0


numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  # преобразуем итератор в список

print(positive_numbers)

true_values = filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()])

for value in true_values:
    print(value)

# Для использования функции reduce() необходимо подключить специальный модуль functools
# Функция reduce() имеет сигнатуру reduce(func, iterable, initializer=None)

from functools import reduce


def func(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(func, numbers, 0)  # в качестве начального значения 0
print(total)


# Модуль operator

from operator import *     #  импортируем все функции

print(add(10, 20))         #  сумма
print(floordiv(20, 3))     #  целочисленное деление
print(neg(9))              #  смена знака
print(lt(2, 3))            #  проверка на неравенство <
print(lt(10, 8))           #  проверка на неравенство <
print(eq(5, 5))            #  проверка на равенство ==
print(eq(5, 9))            #  проверка на равенство ==

from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
concat_words = reduce(operator.add, words)             #  конкатенация элементов списка

print(opposite_numbers)
print(concat_words)