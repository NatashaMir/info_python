def f():
    print("ok1")
    g1=yield 10
    print(g1)
    g2=yield  20
    print(g2)
    g3=yield 30

gen = f()
k1 = next(gen)
print(k1)
k2 = gen.send(400)
print(k2)