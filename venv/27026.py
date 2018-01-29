class My_metaclass(type):
    def __new__(cls, name, base, dirs):
        return type.__new__(cls, name, base, dirs)

    def my_method(cls):
        print("My method!")

class A:
    @staticmethod
    def my_method():
        print("My method from A")

class My_class(A, metaclass=My_metaclass):
    pass



My_class.my_method()