class Point:
    # пространство имен класса
    "Класс для предоставления координат точек на плоскости"
    color = 'red'
    circle = 2


print(Point.__dict__)

# экземпляр клаcса
a = Point()
b = Point()

print(type(a))
print(a.__dict__)
print(type(b))
print(isinstance(a, Point))

a.color = 'black'

Point.type_pt = 'disc' # or
setattr(Point, 'prop', 1)

getattr(Point, 'color', False)

del Point.color

hasattr(Point, 'prop')

print(Point.__doc__)
