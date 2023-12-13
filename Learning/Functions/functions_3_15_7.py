# Анонимные функции
# Общий формат определения анонимной функции: lambda список_параметров: выражение

def standard_function(x):  # стандартное объявление функции
    return x * 2


lambda_function = lambda x: x * 2  # объявление анонимной функции

print(standard_function(7))
print(lambda_function(7))

f1 = lambda: 10 + 20  # функция без параметров
f2 = lambda х, у: х + у  # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z  # функция с тремя параметрами

print(f1())
print(f2(5, 10))
print(f3(5, 10, 30))


# Однократное использование функции

def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))  # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))  # сортируем по сумме кортежа

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))  # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: point[0] + point[1]))  # сортируем по сумме элементов кортежа

# Передача анонимных функций в качестве аргументов другим функциям

numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x + 1, numbers))  # увеличиваем на 1
new_numbers2 = list(map(lambda x: x * 2, numbers))  # удваиваем
new_numbers3 = list(map(lambda x: x ** 2, numbers))  # возводим в квадрат

print(new_numbers1)
print(new_numbers2)
print(new_numbers3)

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x * y, strings, numbers))

print(new_strings)

numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers))  # положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))  # числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # четные числа

print(positive_numbers)
print(large_numbers)
print(even_numbers)

words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))  # слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))  # слова содержащие букву e

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
        return a * x ** 2 + b * x + c

    return square_polynom


def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


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

from functools import reduce


# is_num = lambda x: True if list(filter(lambda y: y == True, map(lambda z: z.isalpha(), [i for i in x]))).count(True) == 0 else False

def analizator(alphas):
    if alphas.count('.') <= 1 and alphas[0] != '.' and alphas[~0] != '.':
        if '-' not in alphas[1:]:
            if True in filter(lambda y: y == True, map(lambda x: x.isalpha(), [i for i in alphas])):
                return False
            # for alpha in alphas:
            #     if alpha.isalpha():
            #         print(False)
            #         return False
        else:
            print(False)
            return False
    else:
        print(False)
        return False
    return True


print("result: ", analizator('10.34ab'))


def is_number(num):
    first = lambda num_1: num_1[0].isdigit() or num_1[0] == '-'
    second = lambda num_2: num_2.count('.') <= 1
    third = lambda num_3: reduce(lambda x, y: x * y,
                                 [num_3[i].isdigit() or num_3[i] == '.' for i in range(1, len(num_3))])
    return first(num) * second(num) * third(num)


# is_num = lambda alphas: True if is_number(alphas) else False
is_num = lambda s: s[0].isdigit() or s[0] == '-' if len(s) == 1 else (s[0].isdigit() or s[0] == '-') and s.count(
    '.') <= 1 and reduce(
    lambda x, y: x * y, [a.isdigit() for a in ''.join(s[1:].split('.'))]) == 1

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('0'))
print(is_num('a.6'))

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday',
         'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday',
         'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate',
         'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle',
         'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

print(*sorted(filter(lambda x: len(x) == 6, words)))

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41,
           80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49,
           78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63,
           74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

# for num in numbers:
#     if num % 2 and num > 47:
#         numbers.remove(num)


# if not num % 2:
#     numbers.append(num // 2)
#     numbers.remove(num)

print(len(numbers))
print(numbers)
print(numbers.count(47))

map(numbers.remove, filter(lambda x: x % 2 and x > 47, numbers))
numbers = list(map(lambda x: x // 2 if not x % 2 else x, numbers))
print(numbers.count(47))

# for i in filter(lambda x: x % 2 and x > 47, numbers):
#     numbers.remove(i)

print(len(numbers))
print(*numbers)


data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

print(*sorted(sorted(data), key=lambda x: len(x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
#               'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
#               'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
#               859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
#               'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
#               'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
#               1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
#
# print(max(mixed_list, key=lambda x: x if type(x) != str else 0))


mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
              70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
              13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
              'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
              'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
              'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]


print(*sorted(sorted(mixed_list, key=lambda x: x if type(x) == int else 0), key=lambda y: y if type(y) == str else ''))


# print(*map(lambda x: 255 - x, [int(num) for num in input().split()]))

print("Задание")

a = [int(num) for num in input().split()]
n = list(range(len(a) - 1, -1, -1))
x = int(input())
print(reduce(lambda xx, yy: xx + yy, list(map(lambda aa, nn: aa * x ** nn, a, n))))
