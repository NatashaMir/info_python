class A:
    sfield=100
    def f(self):
        return  A.sfield

A.sfield=700
print(A.sfield)
print(A.__dict__)
pa=A()
print(pa.sfield)