import collections

def my_abstact(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Interface(type):
    def __new__(cls, name, base, dir):
        print("!!!")
        if len(base) == 0:
            print("In")
            dir['abstact_method_list'] = []
            for key, value in dir.items():
                print("key %s, value is %s" % (key, value))
                if isinstance(value,collections.Callable):
                        if value.__name__ == 'wrapper':
                            dir['abstact_method_list'].append(key)
            print(dir['abstact_method_list'])
        else:
            print(base[0].__dict__)
            for method_name in base[0].__dict__['abstact_method_list']:
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


#class My_classNon(My_interface):
#    pass

my = My_class()
#myNon = My_classNon()
