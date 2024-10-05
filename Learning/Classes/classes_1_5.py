import random
import sys


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, n, m):
        self.array = n
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]
        self.quantity_mines = m

    def show(self):
        for row in self.pole:
            for pole in row:
                if pole.fl_open:
                    if pole.mine:
                        print('*', end=' ')
                    else:
                        print(pole.around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()

    def init(self):
        for _ in range(self.quantity_mines):
            x = random.randint(0, self.array - 1)
            y = random.randint(0, self.array - 1)
            while self.pole[x][y].mine:
                x = random.randint(0, self.array - 1)
                y = random.randint(0, self.array - 1)
            self.pole[x][y].mine = True
        for row in range(self.array):
            for col in range(self.array):
                if not self.pole[row][col].mine:
                    for k in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            try:
                                if row + k >= 0 and col + j >= 0 and self.pole[row + k][col + j].mine:
                                    self.pole[row][col].around_mines += 1
                            except IndexError:
                                pass


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()

sys.exit(999)


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        # print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


#
# pt = Point(1, 1)
# print(pt.__dict__)


class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = "foo bar baz foo1 bar1 baz1".split()
head_obj = ListObject(lst_in[0])
list_objects = [head_obj]
for i in range(1, len(lst_in)):
    curr_obj = ListObject(lst_in[i])
    list_objects.append(curr_obj)
    list_objects[i - 1].link(curr_obj)

print(head_obj.data)
print(head_obj.next_obj.data)
