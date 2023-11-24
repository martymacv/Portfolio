# Функции высшего порядка
from functools import reduce


def high_order_function(func):     # функция высшего порядка, так как принимает функцию
    return func(3)


def double(x):                     # обычная функция = функция первого порядка
    return 2*x


def add_one(x):                    # обычная функция = функция первого порядка
    return x + 1


print(high_order_function(double))
print(high_order_function(add_one))

# Функции высшего порядка для обработки набора данных


# Функция map() для того, чтобы применить одно и то же преобразование к каждому элементу


def f(x):
    return x**2     # тело функции, которая преобразует аргумент x


old_list = [1, 2, 4, 9, 10, 25]
new_list = []
for item in old_list:
    new_item = f(item)
    new_list.append(new_item)

print(old_list)
print(new_list)

# def map(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#
#     return result


def square(x):
    return x**2


def cube(x):
    return x**3


numbers = [1, 2, -3, 4, -5, 6, -9, 0]

strings = list(map(str, numbers))        # используем в качестве преобразователя - функцию str
abs_numbers = list(map(abs, numbers))    # используем в качестве преобразователя - функцию abs

squares = list(map(square, numbers))     # используем в качестве преобразователя - функцию square
cubes = list(map(cube, numbers))         # используем в качестве преобразователя - функцию cube

print(strings)
print(abs_numbers)
print(squares)
print(cubes)


strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']

numbers1 = [int(c) for c in strings]  # используем списочное выражение для преобразования
numbers2 = map(int, strings)          # используем функцию map() для преобразования

print(numbers1)
print(numbers2)

# Цепочки преобразований
numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']

new_numbers = map(abs, map(int, numbers))

print(new_numbers)

# Функция filter(), чтобы отобрать часть элементов списка по определенному критерию
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)  # добавляем элемент item если функция function вернула значение True
#
#     return result


def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10


numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]

large_numbers = filter(is_greater10, numbers)  #  список large_numbers содержит элементы, большие 10

print(large_numbers)


def is_odd(num):
    return num % 2


def is_word_long(word):
    return len(word) > 6


numbers = list(range(15))
words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']

odd_numbers = filter(is_odd, numbers)
large_words = filter(is_word_long, words)

print(odd_numbers)
print(large_words)

# Функция reduce() циклы с агрегацией результата
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#
#     return acc

numbers = [1, 2, 3, 4, 5]

total = 0
product = 1

for num in numbers:
    total += num
    product *= num

print(total)
print(product)


def add(x, y):
    return x+y


def mult(x, y):
    return x*y


numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total)
print(product)