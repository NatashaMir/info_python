class Real:
    def sum(self, a, b):
        return a+b

class Proxy:
    def __init__(self, real):
        self.real = real
        self.list = []

    def sum(self, a, b):
        for l in list:
            if l[0] == a and l[1] == b:
                return l[2]
        result = self.real.sum(a, b)
        self.list.append((a, b, result))
        return result