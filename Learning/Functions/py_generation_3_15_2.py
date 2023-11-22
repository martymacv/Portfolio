# Урок 15.2
# Функции с переменным количеством аргументов
# *args - кортеж значений переменных
# **kwargs - именованные списки значений
# def my_func(num, *args):
#     print(type(args))
#     print(args)
#     print(num)
# my_func()
# my_func(1, 2, 3)
# my_func('a', 'b')
# def my_func(num, *kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     print(num)
# my_func()
# my_func(a=1, b=2)
# my_func(name='Timur', job='Teacher')
# def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
#     pass

# ex.1
def count_args(*args):
    return len(args)
def sq_sum(*args):
    return sum(num**2 for num in args)
def mean(*args):
    valid_args = [num for num in args if type(num) == int or type(num) == float]
    return 0.0 if not len(valid_args) else sum(valid_args) / len(valid_args)
def greet(*args):
    str = ''
    for i in range(len(args)):
        str += args[i]
        if i != len(args) - 1:
            str += ' and '
    str += '!'
    return "Hello, " + str
def print_products(*args):
    valid_args = [arg for arg in args if type(arg) == str and arg != '']
    if len(valid_args):
        for i in range(len(valid_args)):
            print("{}) {}".format(i + 1, valid_args[i]))
    else:
        print('Нет продуктов')
def info_kwargs(**kwargs):
    for key in sorted(kwargs):
        print("{}: {}".format(key, kwargs[key]))


print(count_args(1, 2, 3))
print(sq_sum(1, 2, 3))
print(mean(1, 2, 3.4, "d"))
print(mean())
print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products('', [1, 2], ('Stepik',), '', '', '', 5, True)
info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')