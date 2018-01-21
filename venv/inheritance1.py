import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(point):
         return math.sqrt(point.x*point.x + point.y*point.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius

class Other_circle:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

circle = Circle(10, 20, 100)
print(distance(circle))
print(circle.__dict__)

