import collections

def my_abstact(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Interface(type):
    abstract_method_list = []
    count = 0
    def __new__(cls, name, base, dir):
        print("!!!")
        if Interface.count == 0:
            print("In")
            for key, value in dir.items():
                if isinstance(value,collections.Callable):
                        if value.__name__ == 'wrapper':
                            Interface.abstract_method_list.append(key)
            Interface.count += 1
            print(Interface.abstract_method_list)
        else:
            for method_name in Interface.abstract_method_list:
                print("Methods")
                if not method_name in dir.keys():
                    raise AssertionError()
        return type.__new__(cls, name, base, dir)


class My_interface(metaclass=Interface):

    @my_abstact
    def f1(self):
        pass

    @my_abstact
    def f2(self):
        pass

    def f3(self):
        print("f3")


class My_class(My_interface):

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")


my = My_class()