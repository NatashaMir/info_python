def f():
    a=100
    def g():
        nonlocal a
        a=300
    print(a)
    g()
    print(a)

f()
