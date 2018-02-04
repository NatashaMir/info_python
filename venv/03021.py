class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.instance == None:
            Singleton.instance = object.__new__(cls)
        return Singleton.instance

    def __init__(self):
        pass

single = Singleton()
single1 = Singleton()
print(single)
print(single1)