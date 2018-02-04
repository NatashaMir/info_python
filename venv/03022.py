class Product:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Factory:
    instance = None
    def __new__(cls, *args, **kwargs):
        if Singleton.instance == None:
            Singleton.instance = object.__new__(cls)
        return Singleton.instance

    @staticmethod
    def get_product(a, b, c):
        if a+b < c:
            return None
        return Product(a, b, c)




