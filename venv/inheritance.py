import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
         return math.sqrt(self.x*self.x + self.y*self.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius

circle = Circle(10, 20, 100)
print(circle.distance())
print(circle.__dict__)
circle.distance()
Circle.distance(circle)
