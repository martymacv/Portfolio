# Урок 15.1
# Существуют три типа аргументов у функции: позиционные, именованные и необязательные
# Примеры функций с позиционными и именованными аргументами
# def func(x, y):
#     pass
# func(1, 1)
# func(x=1, y=1) или
# func(1, y=1)
# Примеры функций с необязательными аргументами
# def func(x, y=1):
#     pass
# func(1)
# def func(x, y=None):
#     y = []
#     pass
# func(1)
# func(1, [1, 2])
def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


print(matrix(3, 4, 5))
