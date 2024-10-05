import sys
from functools import reduce
from operator import mul

import random
from datetime import datetime, timedelta

with open("rrrrrr.txt", "r", encoding="utf-8") as fin1:
    rows = fin1.readlines()
    l = []
    for i in range(len(rows)):
        if 'def' in rows[i]:
            if rows[i - 1][0] == '#':
                continue
            else:
                l.append(rows[i])


if len(l):
    l = list(map(lambda x: ''.join(x.split()[1:]), l))
    l = list(map(lambda x: x.split('(')[0], l))
    print(*l, sep='\n')
else:
    print("Best Programming Team")

sys.exit(999)


symbols = {
    'а': 'a', 'к': 'k', 'х': 'h',
    'б': 'b', 'л': 'l', 'ц': 'c',
    'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh',
    'д': 'd', 'о': 'o', 'щ': 'shh',
    'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y',
    'ж': 'zh', 'с': 's', 'ь': '\'',
    'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju',
    'й': 'j', 'ф': 'f', 'я': 'ya'
}

with open("cyrillic.txt", "r", encoding="utf-8") as fin1, open("transliteration.txt", "w", encoding="utf-8") as fin2:
    cyrillic = fin1.read()
    for char in cyrillic:
        if char.lower() in symbols.keys():
            if char.isupper():
                fin2.write(symbols[char.lower()].capitalize())
            else:
                fin2.write(symbols[char])
        else:
            fin2.write(char)


sys.exit(999)


with open("cyrillic.txt", "r", encoding="utf-8") as fin1, open("transliteration.txt", "w", encoding="utf-8") as fin2:
    forbidden_words = fin2.read().split()
    rows1 = fin1.read()
    rows2 = rows1
    for forbidden_word in forbidden_words:
        if forbidden_word in rows2.lower():
            rows2 = rows2.lower().replace(forbidden_word, '*' * len(forbidden_word))
    for i in range(len(rows1)):
        if rows2[i] == '*':
            print('*', end='')
        else:
            print(rows1[i], end='')

# put your python code here
with open("logfile.txt", "r", encoding="utf-8") as fin, open("output.txt", "w", encoding="utf-8") as fout:
    l = list(map(lambda row: row.strip().split(','), fin.readlines()))
    l = list(
        map(lambda t: [t[0], datetime.strptime(t[2].strip(), '%H:%M') - datetime.strptime(t[1].strip(), '%H:%M')], l))
    l = list(filter(lambda t: t[1].seconds >= 3600, l))
    l = list(map(lambda t: t[0], l))
    for name in l:
        fout.writelines(name)
    print(l)

# print(colours[1])
# fout.writelines('\n'.join([f"{name} {int(score) + 5 if int(score) <= 95 else 100}" for name, score in list(map(str.split, fin))]))


goats.txt
input.txt
last_names.txt
lines.txt


def unzip(row):
    return mul(*list(map(int, row.split()[1:])))


with open("prices.txt", "r", encoding="utf-8", errors="ignore") as txt_f:
    print(sum(map(unzip, txt_f.readlines())))
    print(unzip(txt_f.readlines()[0]))

print(random.randint(0, 15))

sys.exit(999)


def func(x):
    pass


ip_addrs = []
for _ in range(int(input())):
    ip_addr = input()
    ip_addrs.append(tuple(map(int, ip_addr.split('.'))) + (ip_addr,))

for ip in sorted(ip_addrs):
    print(ip[4])
sys.exit(999)


def func(x):
    return ord(x) - ord('A')


l = []
for _ in range(int(input())):
    s = input()
    l.append((sum(list(map(func, s.upper()))), s))

print(sorted(l))

sys.exit(999)


def arithmetic_operation(operation):
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    return (operations[operation])


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(f, g):
    def func3(x):
        return f(g(x))

    return func3


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))


def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


def call(func, *args):
    return func(*args)


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

sys.exit(999)

numbers = [(), (10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)

print(sorted_numbers)

numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))

words = 'the world is mine take a look what you have started'.split()


def func(n):
    return '"' + n + '"'


print(*list(map(func, words)))


def product_of_odds(data):
    def func1(m):
        if m % 2 == 1:
            return m

    def func2(n1, n2):
        return n1 * n2

    return reduce(func2, list(filter(func1, data)), 1)


print(product_of_odds([1, 2, 3]))


def concat(*args, sep=' '):
    return sep.join(map(str, args))


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

numbers = [1, 2, 3]
result = reduce(lambda a, b: a * b, numbers, 10)
print(result)


def pretty_print(data, side='-', delimiter='|'):
    s1 = delimiter + ' ' + f' {delimiter} '.join(map(str, data)) + ' ' + delimiter
    ln = len(s1)
    s2 = ' ' + side * (ln - 2) + ' '
    print(f"{s2}\n{s1}\n{s2}")


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
sys.exit(999)


def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f"To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!"


print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))

num = int('1000001', 2)
print(num)
tryings = list()
for _ in range(int(input())):
    tryings.append(tuple(input().split(': ')))
if len(tryings):
    a = len([how for who, how in set(tryings) if how == 'Correct'])
    b = int(len([how for who, how in tryings if how == 'Correct']) / len(tryings) * 100 + 0.5)
    if a:
        print(f'Верно решили {a} учащихся')
        print(f'Из всех попыток {b}% верных')
    else:
        print('Вы можете стать первым, кто решит эту задачу')

school = list()
for _ in range(int(input())):
    school_class = []
    for _ in range(int(input())):
        school_class.append(True if int(input().split()[1]) == 5 else False)
    school.append(any(school_class))
print('YES' if all(school) else 'NO')


def rule(func):
    for ch in password:
        if func(ch):
            return True
    return False


password = input()
rules = [str.isdigit, str.isupper, str.islower]
print('YES' if all(list(map(rule, rules)) + [len(password) >= 7]) else 'NO')

rng = list(map(str, range(int(input()), int(input()) + 1)))
rng = list(filter(lambda x: '0' not in x, rng))
rng = list(filter(lambda x: all(map(lambda y: int(x) % int(y) == 0, x)), rng))
print(*rng)
# print(input().split('.')[3].isnumeric())
ip_addr = input().split('.')
print(all(map(lambda x: 0 <= int(x) <= 255, ip_addr))) if all(map(lambda x: x.isnumeric(), ip_addr)) else print('False')

# ip_addr = all(map(int, filter(lambda x: x.isalnum(), input().split('.'))))

# 0.0 1.0 2.0
# 0.0 0.0 1.1
# 0.0 1.0 1.5
# 0.0 0.0
# 1.5 0.0
# 1.1 1.1

abscissas, ordinates, applicates = [list(map(lambda x: float(x), input().split())) for _ in range(3)]
print(all(list(map(lambda points: 2.0 ** 2 >= points[0] ** 2 + points[1] ** 2 + points[2] ** 2,
                   zip(abscissas, ordinates, applicates)))))


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda word: word in command, ignore))


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        print(word)
        if word in command:
            print(word)
            return True
    return False


# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
print(ignore_command('trancate'))

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
populations = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

# Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате:
# <capital> is the capital of <country>, population equal <population> people.
for capital, country, population in zip(capitals, countries, populations):
    print(f"{capital} is the capital of {country}, population equal {population} people.")
