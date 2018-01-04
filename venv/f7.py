a = 10

def g():
    global a
    a=100

print(a)
g()
print(a)