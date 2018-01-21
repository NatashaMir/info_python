class A:
    def __init__(self, a):
        self.a = a

    def f(self):
        print('a')

class B:
    def __init__(self, b):
        self.b = b

    def f(self):
        print('b')


class C(B, A):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c

c = C(10, 20, 30)
print(c.__dict__)
c.f()