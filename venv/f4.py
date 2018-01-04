def func():
    print("ok1")
    yield 10
    print("ok2")
    yield 20
    print("ok3")
    yield 30


g = func()
print("base1")
k1=next(g)
print(k1)
k2=next(g)
print(k2)