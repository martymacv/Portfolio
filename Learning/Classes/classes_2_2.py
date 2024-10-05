import sys

b = 3
b = b * b
b = b + b * b
print(b)

class TreeObj:  # - для описания вершин и листьев решающего дерева;
    def __init__(self, indx, value=None):
        self.indx = indx  # - проверяемый индекс (целое число);
        self.value = value  # - значение с данными (строка);
        self.__left = None  # - ссылка на следующий объект дерева по левой ветви (изначально None);
        self.__right = None  # - ссылка на следующий объект дерева по правой ветви (изначально None).

    def get_left(self):
        return self.__left

    def set_left(self, left):
        self.__left = left

    def get_right(self):
        return self.__right

    def set_right(self, right):
        self.__right = right

    left = property(get_left, set_left)
    right = property(get_right, set_right)


class DecisionTree:  # - для работы с решающим деревом в целом.

    @classmethod
    def predict(cls, root, x):
        """ для построения прогноза (прохода по решающему дереву) для вектора x
            из корневого узла дерева root (возвращает значение узла - атрибут value). """
        last = root
        for vector in x:
            if (last.right, last.left)[vector] is not None:
                last = (last.right, last.left)[vector]
        return last.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """ для добавления вершин в решающее дерево (метод должен возвращать
            добавленную вершину - объект класса TreeObj);
            obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
            node - ссылка на объект дерева, к которому присоединяется вершина obj;
            left - флаг, определяющий ветвь дерева (объекта node),
            к которой присоединяется объект obj (True - к левой ветви; False - к правой). """
        if node is not None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)


to1 = TreeObj(1, 'The first')
to_left = TreeObj(2, 'The left')
to_right = TreeObj(3, 'The right')
to1.left = to_left
to1.right = to_right

sys.exit(999)

class RadiusVector2D:
    MIN_COORD, MAX_COORD = -100, 1024

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def check_coord(cls, coord):
        return cls.MIN_COORD <= coord <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        x, y = vector.x, vector.y
        return x * x + y * y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if self.check_coord(x):
            self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if self.check_coord(y):
            self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)


v1 = RadiusVector2D()
v2 = RadiusVector2D(1)
v3 = RadiusVector2D(1, 2)

sys.exit(999)

class StackObj:
    def __init__(self, data):
        self.__data = data  # - ссылка на строку с данными, указанными при создании объекта
        self.__next = None  # - ссылка на следующий объект класса StackObj

    @staticmethod
    def check_next(stack_obj):
        return type(stack_obj) == StackObj or type(stack_obj) == None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    data = property(get_data, set_data)
    next = property(get_next, set_next)


class Stack:
    def __init__(self):
        self.top = None

    def find_last(self) -> tuple:
        prev = None
        curr = self.top
        next = curr.next
        while next is not None:
            prev = curr
            curr = next
            next = next.next
        return prev, curr

    def create_list(self) -> list:
        st_objs = []
        curr = self.top
        while curr is not None:
            st_objs.append(curr.data)
            curr = curr.next
        return st_objs

    def push(self, obj):  # - добавление объекта класса StackObj в конец односвязного списка;
        if self.top is None:
            self.top = obj
        else:
            self.find_last()[1].next = obj

    def pop(self):  # - извлечение последнего объекта с его удалением из односвязного списка;
        if self.top is None:
            return None
        else:
            prev = self.find_last()[0]
            curr = self.find_last()[1]
            if curr.next is None and prev is None:
                obj = self.top
                self.top = None
                return obj
            else:
                prev.next = None
            return curr

    def get_data(self):  # - получение списка из объектов односвязного списка.
        return self.create_list()


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']

sys.exit(999)

class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @staticmethod
    def check(param):
        return type(param) == int and 0 <= param <= 10000

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        if self.check(width):
            self.__width = width
            self.show()

    def set_height(self, height):
        if self.check(height):
            self.__height = height
            self.show()

    width = property(get_width, set_width)
    height = property(get_height, set_height)


wnd = WindowDlg("заголовок окна", 33, 55)
wnd.show()
wnd.width = 10001
sys.exit(999)


class Car:
    def __init__(self, model=None):
        self.__model = None

    @staticmethod
    def check_model(model):
        return type(model) == str and 2 <= len(model) <= 100

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if self.check_model(model):
            self.__model = model

    model = property(get_model, set_model)


car = Car()
car.model = 'abc'
car.model = 'a'
print(car.model)
