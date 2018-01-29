class My_metaclass(type):
    def __new__(cls, name, base, dir):
        print("New from Metaclass")
        print(dir)
        return type.__new__(cls, name, base, dir)

    def __init__(cls, name, base, dir):
        print("Init from Metaclass")

class My_class(metaclass=My_metaclass):
    def __new__(cls, *args, **kwargs):
        print("New from class")
        return object.__new__(cls)

    def __init__(self):
        print("Init from class")

    def my_method(self):
        print("My method")

class Inheritance_my_class(My_class):
    pass

myclass = Inheritance_my_class()

