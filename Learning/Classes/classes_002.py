class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        print("вызов метода set_coords " + str(self))
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt2 = Point()

pt.set_coords(1, 3) # or
Point.set_coords(pt, 2, 4)
pt2.set_coords(10, 30)

print(pt.__dict__)
print(pt2.__dict__)

print(pt.get_coords())
