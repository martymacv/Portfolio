# Урок 15.4
# Функции, как замена длинным if...elif
# Функции, как аргументы функций
# def hello():
#     print('Hello from function')
# print(type(hello))
#
# writeln = print            # как в языке Pascal 😀
# writeln('Hello world!')
# writeln('Python')
#
# def start():
#     # тело функции start
#     pass
# def stop():
#     # тело функции stop
#     pass
# def pause():
#     # тело функции pause
#     pass
# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
# command = input()  # считываем название команды
# commands[command]()  # вызываем нужную функцию через словарь по ключу
#
# Функции в качестве аргументов других функций
# Определим функцию plot(), которая принимает 3 аргумента:
# f – функцию, для которой хотим построить график,
# и a, b – границы диапазона построения графика.
# def plot(f, a, b):
# def square_add_one(x):
#     return x * x + 1
# def cube_add_square(x):
#     return x ** 3 + x ** 2
# plot(square_add_one, 1, 10)
# plot(cube_add_square, -10, 10)

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers))
print(min(numbers))
print(sorted(numbers))

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers, key=abs))  # указываем функцию abs в качестве компаратора
print(min(numbers, key=abs))  # указываем функцию abs в качестве компаратора
print(sorted(numbers, key=abs))  # указываем функцию abs в качестве компаратора

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
points.sort()  # сортируем список точек на месте
print(points)


def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))  # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))  # сортируем по сумме кортежа


# Функции в качестве возвращаемых значений других функций


def generator():
    def hello():
        print('Hello from function!')

    return hello


func = generator()
func()


def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom


f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))


def comparator(item):
    return item[0]


data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
data.sort(key=comparator)   # сортируем по первому полю

print(data)