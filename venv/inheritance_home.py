import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(Point):
    def __init__(self, x1, y1, x2, y2, length):
        Point.__init__(self, x1, y1)
        Point.__init__(self, x2, y2)
        self.length = length

    def length_line(self):
        return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))


class Quadrilateral:
    def __init__(self, number_lines = 3, number_angles = 3):
        self.lines = [0 for i in range(number_lines)]
        self.angles = [0 for i in range(number_angles)]

    def input_line(self, line):
        self.lines.append(line)

    def input_angle(self, angle):
        self.angles.append(angle)

class Parallelogram(Quadrilateral):
    def __init__(self, lines, angles):
        Quadrilateral.__init__(self, 2, 1)

class Rectangle(Parallelogram):
    def __init__(self, lines):
        Parallelogram.__init__(self, 2, 0)

class Rhombus(Parallelogram):
    def __init__(self, lines, angles):
        Parallelogram.__init__(self, 1, 1)

class Square(Rectangle):
    def __init__(self, lines):
        Rectangle.__init__(self, 1)

quadrilateral = Quadrilateral()
print(quadrilateral.__dict__)

parallelogram = Parallelogram(4, 1)
print(parallelogram.__dict__)

rhombus = Rhombus(1, 1)
print(rhombus.__dict__)

square = Square(1)
print(square.__dict__)
