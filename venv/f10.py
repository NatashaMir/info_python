class A:
    def __init__(self):
        self.a=10
        self.b=20;
    def sum(self):
        return self.a+self.b

#pa=A()
#pa.sum()
pa=A.__new__(A)
A.__init__(pa)
print(pa.__dict__)
print(A.__dict__)
A.sum(pa)
A.__dict__["sum"].__call__(pa)

