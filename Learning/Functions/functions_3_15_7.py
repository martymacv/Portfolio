# Анонимные функции
# Общий формат определения анонимной функции: lambda список_параметров: выражение

def standard_function(x):  # стандартное объявление функции
    return x * 2


lambda_function = lambda x: x * 2  # объявление анонимной функции

print(standard_function(7))
print(lambda_function(7))


f1 = lambda: 10 + 20               # функция без параметров
f2 = lambda х, у: х + у            # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами

print(f1())
print(f2(5, 10))
print(f3(5, 10, 30))

# Однократное использование функции

def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа


# Передача анонимных функций в качестве аргументов другим функциям

numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x+1, numbers))      #  увеличиваем на 1
new_numbers2 = list(map(lambda x: x*2, numbers))      #  удваиваем
new_numbers3 = list(map(lambda x: x**2, numbers))     #  возводим в квадрат

print(new_numbers1)
print(new_numbers2)
print(new_numbers3)

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x*y, strings, numbers))

print(new_strings)

numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа

print(positive_numbers)
print(large_numbers)
print(even_numbers)

words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e

print(new_words1)
print(new_words2)

from functools import reduce

words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)
print(product)
print(sentence)


# Возвращение функции в качестве результата другой функции

def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom


def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c


# Условный оператор в теле анонимной функции

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))

print(result)


# Передача аргументов в анонимную функцию

f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z


print(f1(1, 2, 3))
print(f2(1, 2))
print(f2(1, y=2))
print(f3(1, 2, 3, 4, 5))
print(f4(one=1, two=2, three=3))
print(f5(1))
print(f5(1, y=2, z=3))

