class B:
    def g(self):
        print("G")

A = type('my_class', (B,), {'f' : lambda self, x : x+1})
p = A()
print(p.f(10))
print(A.__name__)
p.g()
eval()